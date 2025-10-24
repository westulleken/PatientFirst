from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Initialize the database object here but don't bind it yet
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

    # Initialize SQLAlchemy with this app
    db.init_app(app)

    # Import models so SQLAlchemy is aware of them
    from models import User

    # Register blueprints
    from routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Create tables
    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        return {"message": "PatientFirst backend is running"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
