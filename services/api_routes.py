from flask import request, redirect, url_for
from services.db_users import get_user, insert_user, update_user, delete_user

VERSION = 1
BASE_API_URL = f'/api/v{VERSION}/'

def register_api_routes(app):
    """
    Registers API routes with the provided Flask application instance.

    :param app: The Flask application instance to register routes with.
    :return: None
    """

    @app.route('/user/add', methods=['POST'])
    def api_add_user():
        """
        Registers API routes with the provided Flask application instance.

        :return: None
        """
        username = request.form['username']
        email = request.form['email']
        insert_user(username, email)
        return redirect(url_for('users_list'))

    @app.route('/user/edit/<int:user_id>', methods=['POST'])
    def api_update_user(user_id):
        """
        :param user_id: The unique identifier for the user to be edited.
        :return: A redirect to a list of users if successful, or a 404 error if the user is not found.
        """
        user = get_user(user_id)
        if not user:
            return "User not found", 404

        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            update_user(user_id, username, email)
            return redirect(url_for('users_list'))

    @app.route('/user/delete/<int:user_id>', methods=['POST'])
    def api_delete_user(user_id):
        user = get_user(user_id)
        if not user:
            return "User not found", 404

        if request.method == 'POST':
            delete_user(user_id)
            return redirect(url_for('users_list'))

