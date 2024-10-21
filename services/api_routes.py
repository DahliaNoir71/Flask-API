from flask import request, redirect, url_for, flash
from services.db_users import *

VERSION = 1
BASE_API_URL = f'/api/v{VERSION}/'

def register_api_routes(app):
    """
    Registers API routes with the provided Flask application instance.

    :param app: The Flask application instance to register routes with.
    :return: None
    """

    @app.route('/user/add', methods=['GET', 'POST'])
    def api_add_user():
        """
        Registers API routes with the provided Flask application instance.

        :return: None
        """
        username = request.form['username']
        email = request.form['email']
        if check_email_unicity(email):
            insert_user(username, email)
            return redirect(url_for('users_list'))
        else:
            flash(f"Email '{email}' is already in use. Please choose a different email.", 'error')
            return redirect(url_for('add_user_form'))



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
            if check_email_unicity(email):
                update_user(user_id, username, email)
                return redirect(url_for('users_list'))
            else:
                flash(f"Email '{email}' is already in use. Please choose a different email.", 'error')
                return redirect(url_for('edit_user_form', user_id = user_id))

    @app.route('/user/delete/<int:user_id>', methods=['POST'])
    def api_delete_user(user_id):
        user = get_user(user_id)
        if not user:
            return "User not found", 404

        if request.method == 'POST':
            delete_user(user_id)
            flash(f'Utilisateur avec ID {user_id} supprimé avec succès!', 'success')
            return redirect(url_for('users_list'))

