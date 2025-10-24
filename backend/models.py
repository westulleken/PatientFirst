from app import db

# ------------------------
# Patient Model
# ------------------------
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(20))
    gender = db.Column(db.String(20))

    def __repr__(self):
        return f"<Patient {self.first_name} {self.last_name}>"

# ------------------------
# User Model
# ------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), default="user")

    def __repr__(self):
        return f"<User {self.username}>"
