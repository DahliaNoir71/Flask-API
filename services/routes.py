from flask import render_template, flash
from services.database import get_users


def register_routes(app):
    """
    :param app: The Flask application instance to which routes are being registered.
    :return: None
    """

    @app.route('/users')
    def users_list():
        users = get_users()
        print(users)
        return render_template('users_list.html', users=users)

    @app.route('/add_user_form')
    def add_user_form():
        return render_template('add_user_form.html')
