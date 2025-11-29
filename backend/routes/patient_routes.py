from flask import Blueprint, request, jsonify
from models.patient import Patient

patient_bp = Blueprint("patient_bp", __name__)

@patient_bp.route("/patients", methods=["POST"])
def create_patient():
    data = request.json
    try:
        patient_id = Patient.create(data)
        return jsonify({"status": "success", "patient_id": patient_id}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
