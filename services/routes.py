from flask import render_template


def register_routes(app):
    """
    :param app: The Flask application instance to which routes are being registered.
    :return: None
    """
    @app.route('/', methods=['GET'])
    def home():
        """
        Registers the routes for the given Flask application `app`.

        :param app: The Flask application instance.
        :return: None
        """
        return render_template('home.html')
