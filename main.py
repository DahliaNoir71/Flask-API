from flask import Flask
from services.routes import register_routes
from services.api_routes import register_api_routes
from services.database import init_db

app = Flask(__name__)

register_api_routes(app)
register_routes(app)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)