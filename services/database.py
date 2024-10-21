import sqlite3
from services.db_users import create_table_users

DB_NAME = "users.db"

def get_db_connection(db_name):
    """
    :param db_name: The name of the SQLite database to connect to.
    :type db_name: str
    :return: A connection object to the SQLite database with `row_factory` set to `sqlite3.Row` for accessing rows as dictionaries.
    :rtype: sqlite3.Connection
    """
    connection = sqlite3.connect(db_name)
    connection.row_factory = sqlite3.Row
    return connection

def create_tables(connection):
    """
    :param connection: Database connection object used to execute SQL commands
    :return: None
    """
    create_table_users(connection)

def init_db():
    """
    Initializes the database by establishing a connection and creating necessary tables.

    :return: None
    """
    sql_connection = get_db_connection(DB_NAME)
    create_tables(sql_connection)





