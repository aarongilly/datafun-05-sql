import pathlib
import common_sql_funcs as my_func
from utils_logger import logger
from db01_setup import do_setup

# Define the database file in the current root project directory
db_file = pathlib.Path("data/workouts_db.sqlite3")

def main():
    # Logging startup
    logger.info('Starting database setup...')
    
    # Adding to make it possible to run db02 without first running db01 
    do_setup()

    logger.info('Adding features...')
    try:
        con = my_func.get_connection(db_file)
        my_func.execute_sql("sql_features/update_records.sql", con)
        print('Column added, records updated')
        my_func.execute_sql("sql_features/delete_records.sql", con)
        print('Records deleted')

    except Exception as e:
        logger.error(f"Error occurred in main: {e}")
    finally:
        con.close()
        logger.info(f"Closed connection to {db_file}")

def do_setup_and_add_features():
    '''
    This function is for reuse on import to other files
    '''
    main()

if __name__ == "__main__":
    main()