from services.database import get_db_connection, DB_NAME

USERS_REQUESTS = {
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
    """,
    "get_user": """
        SELECT
            id, username, email 
        FROM 
            Users 
        WHERE 
            id = :user_id
    """
}

def create_table_users(connection):
    connection.execute(USERS_REQUESTS["create_users_table"])

def get_users():
    """
    :return: A list of user records from the database.
    """
    sql_connection = get_db_connection(DB_NAME)
    users = sql_connection.execute(USERS_REQUESTS["get_users"]).fetchall()
    sql_connection.close()
    return users


def get_user(user_id):
    """
    :param user_id: The ID of the user to retrieve.
    :return: The user information as a dictionary if found, otherwise None.
    """
    sql_connection = get_db_connection(DB_NAME)
    user = sql_connection.execute(USERS_REQUESTS["get_user"], {"user_id": user_id}).fetchone()
    sql_connection.close()
    return user


def insert_user(username, email):
    """
    :param username: The username of the user to be inserted into the database.
    :param email: The email address of the user to be inserted into the database.
    :return: None
    """
    sql_connection = get_db_connection(DB_NAME)
    sql_connection.execute(USERS_REQUESTS["insert_user"],
                           {"username": username, "email": email})
    sql_connection.commit()
    sql_connection.close()


def update_user(user_id, username, email):
    """
    :param user_id: Unique identifier for the user to be updated
    :param username: New username for the user
    :param email: New email address for the user
    :return: None
    """
    sql_connection = get_db_connection(DB_NAME)
    sql_connection.execute(USERS_REQUESTS["update_user"],
                           {"user_id": user_id, "username": username, "email": email})
    sql_connection.commit()
    sql_connection.close()