from flask import Blueprint, request, jsonify
from app import db
from models import Patient

patients_bp = Blueprint('patients', __name__, url_prefix='/patients')

# ------------------------
# GET all patients
# ------------------------
@patients_bp.route('/', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    results = [
        {
            "id": p.id,
            "first_name": p.first_name,
            "last_name": p.last_name,
            "date_of_birth": p.date_of_birth,
            "gender": p.gender
        }
        for p in patients
    ]
    return jsonify(results), 200

# ------------------------
# POST new patient
# ------------------------
@patients_bp.route('/', methods=['POST'])
def add_patient():
    data = request.get_json()
    try:
        new_patient = Patient(
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data.get('date_of_birth'),
            gender=data.get('gender')
        )
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"message": "Patient added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
