from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Create global SQLAlchemy instance
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app)

    # ----------------------------
    # Database configuration
    # ----------------------------
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///patientfirst.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database
    db.init_app(app)

    # ----------------------------
    # Import and register blueprints
    # ----------------------------
    from routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Optional: add future blueprints here (e.g. /patients, /appointments)

    # ----------------------------
    # Create database tables
    # ----------------------------
    with app.app_context():
        from models import User  # ensure models are registered before create_all
        db.create_all()

    # ----------------------------
    # Root route
    # ----------------------------
    @app.route("/")
    def index():
        return {"message": "PatientFirst backend is running"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
