from flask import Blueprint, jsonify, request
from utils.db import get_db_connection

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/auth', methods=['GET'])
def authenticated_route():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Cette route est authentifiée'")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify({"message": result[0]})

