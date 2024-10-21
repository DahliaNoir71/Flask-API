from flask import render_template, flash
from services.database import get_users


def register_routes(app):
    """
    :param app: The Flask application instance to register routes on.

    :return: None
    """

    @app.route('/')
    @app.route('/users')
    def users_list():
        """
        Registers the routes for the web application.

        :param app: The Flask application instance to register routes on.

        The function sets up the following routes:
        - "/" and "/users" which renders the list of users.

        :return: None
        """
        users = get_users()
        return render_template('users_list.html', users=users)

    @app.route('/add_user_form')
    def add_user_form():
        """
        Registers the route for adding a user form to the given Flask application.

        :param app: The Flask application instance
        :return: None
        """
        return render_template('add_user_form.html')
