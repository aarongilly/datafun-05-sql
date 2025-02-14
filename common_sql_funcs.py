import sqlite3
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
