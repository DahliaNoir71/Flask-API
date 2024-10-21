from flask import request, redirect, url_for
from services.db_users import get_users, get_user, insert_user

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

    @app.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
    def update_user(user_id):
        user = get_user(user_id)
        if not user:
            return "User not found", 404

        if request.method == 'POST':
            user['username'] = request.form['username']
            user['email'] = request.form['email']
            user['phone'] = request.form['phone']
            user['address'] = request.form['address']
            return redirect(url_for('update_user', user_id=user_id))

