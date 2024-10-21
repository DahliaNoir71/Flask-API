import sqlite3

DB_NAME = "users.db"

SQL_REQUESTS = {
    "create_users_table": """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT
        )
    """,
    "get_users": """
        SELECT 
            id, username, email
        FROM 
            Users
    """,
    "insert_user": """
        INSERT INTO Users 
            (username, email)
        VALUES
            (:username, :email)
    """
}

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
    connection.execute(SQL_REQUESTS["create_users_table"])

def init_db():
    """
    Initializes the database by establishing a connection and creating necessary tables.

    :return: None
    """
    sql_connection = get_db_connection(DB_NAME)
    create_tables(sql_connection)

def get_users():
    """
    :return: A list of user records from the database.
    """
    sql_connection = get_db_connection(DB_NAME)
    users = sql_connection.execute(SQL_REQUESTS["get_users"]).fetchall()
    sql_connection.close()
    return users

def insert_user(username, email):
    """
    :param username: The username of the user to be inserted into the database.
    :param email: The email address of the user to be inserted into the database.
    :return: None
    """
    sql_connection = get_db_connection(DB_NAME)
    sql_connection.execute(SQL_REQUESTS["insert_user"], {"username": username, "email": email})
    sql_connection.commit()
    sql_connection.close()



