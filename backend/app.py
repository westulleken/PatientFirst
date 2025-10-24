from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///patientfirst.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # ------------------------
    # Import and register blueprints
    # ------------------------
    from routes.patients import patients_bp
    app.register_blueprint(patients_bp)

    @app.route('/')
    def index():
        return {"message": "PatientFirst backend is running"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
