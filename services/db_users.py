from services.database import get_db_connection, DB_NAME

USERS_REQUESTS = {
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
    """,
    "update_user":
    """
    UPDATE 
        Users
    SET 
        username = :username, email = :email
    WHERE 
        id = :user_id
    """,
    "delete_user": "DELETE FROM Users WHERE id = :user_id"
}

def get_users():
    """
    Fetches the list of users from the database.

    :return: A list of user records from the database.
    """
    sql_connection = get_db_connection(DB_NAME)
    users = sql_connection.execute(USERS_REQUESTS["get_users"]).fetchall()
    sql_connection.close()
    return users


def get_user(user_id):
    """
    :param user_id: ID of the user to fetch from the database
    :return: User record from the database
    """
    sql_connection = get_db_connection(DB_NAME)
    user = sql_connection.execute(USERS_REQUESTS["get_user"], {"user_id": user_id}).fetchone()
    sql_connection.close()
    return user


def insert_user(username, email):
    """
    :param username: The name of the user to be inserted into the database.
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
    :param user_id: The unique identifier for the user to be updated.
    :param username: The new username to set for the user.
    :param email: The new email to set for the user.
    :return: None
    """
    sql_connection = get_db_connection(DB_NAME)
    sql_connection.execute(USERS_REQUESTS["update_user"],
                           {"user_id": user_id, "username": username, "email": email})
    sql_connection.commit()
    sql_connection.close()

def delete_user(user_id):
    """
    :param user_id: The ID of the user to delete from the database.
    :return: None
    """
    sql_connection = get_db_connection(DB_NAME)
    sql_connection.execute(USERS_REQUESTS["delete_user"], {"user_id": user_id})
    sql_connection.commit()
    sql_connection.close()