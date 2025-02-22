import pathlib
import common_sql_funcs as my_func
from utils_logger import logger

# Define the database file in the current root project directory
db_file = pathlib.Path("data/workouts_db.sqlite3")

def main():
    # Logging startup
    logger.info('Starting database setup...')
    try:
        con = my_func.get_connection(db_file)
        my_func.execute_sql("sql_create/01_drop_tables.sql", con)
        print('Tables Dropped')
        my_func.execute_sql("sql_create/02_create_tables.sql", con)
        print('Tables Created')
        my_func.execute_sql("sql_create/03_insert_records.sql", con)
        print('Records inserted')

    except Exception as e:
        logger.error(f"Error occurred in main: {e}")
    finally:
        con.close()
        logger.info(f"Closed connection to {db_file}")

def do_setup():
    '''
    This function is for reuse on import to other files
    '''
    main()

if __name__ == "__main__":
    main()
