from flask import jsonify
from services.employees import employees

VERSION = 1
BASE_API_URL = f'/api/v{VERSION}/resources/'

def register_api_routes(app):

    @app.route(BASE_API_URL + 'employees/all', methods=['GET'])
    def api_employees_all():
        return jsonify(employees)