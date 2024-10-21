from flask import request, redirect, url_for
from services.database import insert_user

VERSION = 1
BASE_API_URL = f'/api/v{VERSION}/'

def register_api_routes(app):
    """
    :param app: The flask application instance where the API routes will be registered.
    :return: None
    """

    @app.route('/add_user', methods=['POST'])
    def add_user():
        """
        Registers API routes with the provided Flask application instance.

        :return: None
        """
        username = request.form['username']
        email = request.form['email']
        insert_user(username, email)
        return redirect(url_for('users_list'))


