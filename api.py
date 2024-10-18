from flask import Flask
from services.routes import register_routes
from services.api_routes import register_api_routes

app = Flask(__name__)

register_api_routes(app)
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)