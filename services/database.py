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
    :param db_name: Name of the database file to connect to
    :return: A tuple containing the database connection and the cursor.
    """
    connection = sqlite3.connect(db_name)
    connection.row_factory = sqlite3.Row
    return connection

def create_tables(connection):
    """
    :param cursor: The cursor used to interact with the database.
    :return: None
    """
    connection.execute(SQL_REQUESTS["create_users_table"])

def init_db():
    sql_connection = get_db_connection(DB_NAME)
    create_tables(sql_connection)

def get_users():
    sql_connection = get_db_connection(DB_NAME)
    users = sql_connection.execute(SQL_REQUESTS["get_users"]).fetchall()
    sql_connection.close()
    return users

def insert_user(username, email):
    sql_connection = get_db_connection(DB_NAME)
    sql_connection.execute(SQL_REQUESTS["insert_user"], {"username": username, "email": email})
    sql_connection.commit()
    sql_connection.close()



