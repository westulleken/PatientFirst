@app.route("/admin/dropdowns")
def admin_dropdowns():
    return render_template("admin_dropdowns.html")
from flask import render_template
from flask import Flask
from flask_cors import CORS

from routes.patient_routes import patient_bp
from routes.dropdown_routes import dropdown_bp

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(patient_bp, url_prefix="/api")
app.register_blueprint(dropdown_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"status": "PatientFirst EMR backend running"}

if __name__ == "__main__":
    app.run(debug=True)
