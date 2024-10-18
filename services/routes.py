from flask import render_template


def register_routes(app):

    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')
