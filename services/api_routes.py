from flask import jsonify
from services.employees import employees

VERSION = 1
BASE_API_URL = f'/api/v{VERSION}/resources/'

def register_api_routes(app):
    """
    :param app: The flask application instance where the API routes will be registered.
    :return: None
    """
    @app.route(BASE_API_URL + 'employees/all', methods=['GET'])
    def api_employees_all():
        """
        Register API routes for the provided Flask application.

        :return: None
        """
        return jsonify(employees)

    @app.route(BASE_API_URL + 'employees/<int:id_employee>', methods=['GET'])
    def api_employees_id(id_employee):
        """
        :param id_employee: The unique identifier for an employee.
        :return: A JSON response containing the details of the employee with the given id.
        """
        result = []
        for employee in employees:
            if employee['id'] == id_employee:
                result.append(employee)

        return jsonify(result)

