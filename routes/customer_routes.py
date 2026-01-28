from flask import Blueprint, request, jsonify
from services.customer_service import *

customer_bp = Blueprint('customer_bp', __name__)

# CREATE
@customer_bp.route('/customers', methods=['POST'])
def add_customer_route():
    data = request.json
    return jsonify(add_customer(data))

# READ ALL
@customer_bp.route('/customers', methods=['GET'])
def get_customers_route():
    return jsonify(get_all_customers())

# READ ONE
@customer_bp.route('/customers/<int:id>', methods=['GET'])
def get_customer_route(id):
    return jsonify(get_customer_by_id(id))

# UPDATE
@customer_bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer_route(id):
    data = request.json
    return jsonify(update_customer(id, data))

# DELETE
@customer_bp.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer_route(id):
    return jsonify(delete_customer(id))
