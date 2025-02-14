import pathlib
import common_sql_funcs as my_func
import pandas as pd
import seaborn as sns
import sqlite3

from utils_logger import logger
from db02_features import do_setup_and_add_features

# Define the database file in the current root project directory
db_file = pathlib.Path("data/workouts_db.sqlite3")

def query_to_dataframe(path, connection) -> pd.DataFrame:
    '''
    Executes a query contained in the file at the passed-in path
    and loads the result to a Pandas DataFrame.

    Args:
        path (str): Path to the SQL file
        connect (sqlite3.Connection): existing connection to a database
    '''
    try:
        logger.info(f'Executing SQL stored at {path}...')
        with open(path, 'r') as file:
            sql_script: str = file.read()
            logger.info('File read successfully')
        with connection:
            logger.info('SQL executed successfully')
            cursor = connection.cursor()
            cursor.execute(sql_script)
            results = cursor.fetchall()
            df_results = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
            return df_results
        
    except Exception as e:
        logger.error(f"Failed to execute SQL at {path}, with error: {e}")
        raise


def execute_multiple_queries(sql_file_path, con):
    try:
        cursor = con.cursor()

        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        # Split the script into individual statements
        statements = sql_script.split(';')

        results = []  # Store the results of each query

        for statement in statements:
            # Skip empty statements
            if statement.strip():
                cursor.execute(statement)
                try:
                    result = cursor.fetchall()  # Get all rows for SELECT statements
                    results.append(result)
                except sqlite3.OperationalError:  # For non-SELECT statements (e.g., INSERT, UPDATE)
                    con.commit()  # Commit changes after non-SELECT
                    results.append(None) # Append None as there is no result to append
                    pass # Or handle the non-SELECT as needed

        return results

    except Exception as e:
        print(f"Error executing queries: {e}")
        return None


def main():
    # Logging startup
    logger.info('Starting database setup...')

    # Adding to make it possible to run db03 without first running db01 or db02 
    do_setup_and_add_features()

    try:
        con = my_func.get_connection(db_file)
        basic_query = query_to_dataframe('sql_queries/query_filter.sql', con)
        print(basic_query)

        # Execute multiple queries, loading result of each to list
        # This feels very wrong, surely not a typical approach to getting
        # data from SQL into python variables
        multiple_selects = execute_multiple_queries('sql_queries/query_aggregation.sql', con)
        print(multiple_selects)

        grouped_query = query_to_dataframe('sql_queries/query_group_by.sql', con)
        print(grouped_query)

        sorted_query = query_to_dataframe('sql_queries/query_sorting.sql', con)
        print(sorted_query)

        # Execute multiple queries, loading result of each to list
        multiple_joined_selects = execute_multiple_queries('sql_queries/query_join.sql', con)
        print(multiple_joined_selects)

        # Doing an inline query using python's standard sqlite library
        # I assume this would be a slightly more common method of getting data
        # from a database into python variables, it's more localised & readable
        cursor = con.cursor()
        cursor.execute('SELECT * FROM workout_events WHERE workout_duration_mins > 31')
        inline_query = cursor.fetchall()
        df_results = pd.DataFrame(inline_query, columns=[desc[0] for desc in cursor.description])
        
        # Plotting the results
        sns.barplot(x='workout_duration_mins', y='workout_name', data=df_results)

        print(df_results)
        
    except Exception as e:
        logger.error(f"Error occurred in main: {e}")
    finally:
        con.close()
        logger.info(f"Closed connection to {db_file}")

if __name__ == "__main__":
    main()