from flask import Blueprint, jsonify

public_routes = Blueprint('public_routes', __name__)

@public_routes.route('/public', methods=['GET'])
def public_route():
    return jsonify({"message": "Cette route est publique"})

