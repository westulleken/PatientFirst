from .db import get_db_connection

class Dropdown:

    @staticmethod
    def get_all(table):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table} ORDER BY 1 ASC;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    @staticmethod
    def insert(table, column, value):
        conn = get_db_connection()
        cur = conn.cursor()

        sql = f"INSERT INTO {table} ({column}) VALUES (%s) RETURNING *;"
        cur.execute(sql, (value,))
        result = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        return result
