from flask import Blueprint, jsonify, request
from models.dropdown import Dropdown

dropdown_bp = Blueprint("dropdown_bp", __name__)

# Get all values from a dropdown table
@dropdown_bp.route("/dropdown/<table>", methods=["GET"])
def get_dropdown(table):
    try:
        result = Dropdown.get_all(table)
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Insert a new value into a dropdown table
@dropdown_bp.route("/dropdown/<table>", methods=["POST"])
def insert_dropdown(table):
    payload = request.json
    try:
        column = payload.get("column")
        value = payload.get("value")
        result = Dropdown.insert(table, column, value)
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
