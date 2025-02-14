import sqlite3
import pathlib
from utils_logger import logger

def get_connection(path) -> sqlite3.Connection:
    '''
    Opens a connection to the file at the supplied path.

    Args:
        path (str): Path to the sqlite3 database file
    '''
    try:
        logger.info(f'Connecting to database at {path}...')
        return sqlite3.connect(path)
    except Exception as e:
        logger.error(f"Failed to get connection to path {path}, with error: {e}")
        raise

def execute_sql(path, connection) -> None:
    '''
    Opens a sql file & executes its contents against the passed-in connection

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
            connection.executescript(sql_script)
            logger.info('SQL executed successfully')
        
    except Exception as e:
        logger.error(f"Failed to execute SQL at {path}, with error: {e}")
        raise

# Define the database file in the current root project directory
db_file = pathlib.Path("data/workouts_db.sqlite3")

def main():
    # Logging startup
    logger.info('Starting database setup...')
    try:
        con = get_connection(db_file)
        execute_sql("sql_create/01_drop_tables.sql", con)
        print('Tables Dropped')
        execute_sql("sql_create/02_create_tables.sql", con)
        print('Tables Created')
        execute_sql("sql_create/03_insert_records.sql", con)
        print('Records inserted')

    except Exception as e:
        logger.error(f"Error occurred in main: {e}")
    finally:
        con.close()
        logger.info(f"Closed connection to {db_file}")

if __name__ == "__main__":
    main()