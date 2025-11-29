from .db import get_db_connection
import uuid

class Patient:

    @staticmethod
    def create(data):
        conn = get_db_connection()
        cur = conn.cursor()

        patient_id = str(uuid.uuid4())

        sql = """
        INSERT INTO patient (
            patient_id, first_name, surname, salutation_id, id_type_id,
            id_number, date_of_birth, sex_id, gender_identity_id,
            nationality_id, language_id, occupation
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING patient_id;
        """

        cur.execute(sql, (
            patient_id,
            data["first_name"],
            data["surname"],
            data["salutation_id"],
            data["id_type_id"],
            data["id_number"],
            data["date_of_birth"],
            data["sex_id"],
            data["gender_identity_id"],
            data["nationality_id"],
            data["language_id"],
            data["occupation"]
        ))

        conn.commit()
        cur.close()
        conn.close()

        return patient_id
