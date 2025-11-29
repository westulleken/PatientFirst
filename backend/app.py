from flask import Flask, render_template
from flask_cors import CORS

from routes.patient_routes import patient_bp
from routes.dropdown_routes import dropdown_bp

app = Flask(__name__, template_folder="../frontend/templates")
CORS(app)

# Blueprints
app.register_blueprint(patient_bp, url_prefix="/api")
app.register_blueprint(dropdown_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"status": "PatientFirst EMR backend running"}

# Admin dropdown UI
@app.route("/admin/dropdowns")
def admin_dropdowns():
    return render_template("admin_dropdowns.html")

# Patient registration UI
@app.route("/register")
def register():
    return render_template("register_patient.html")

if __name__ == "__main__":
    app.run(debug=True)
