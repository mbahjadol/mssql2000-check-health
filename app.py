from flask import Flask, jsonify
import pyodbc
import os

app = Flask(__name__)

MSSQL_USER = os.getenv("MSSQL_USER", "sa")
MSSQL_PASS = os.getenv("MSSQL_PASS", "yourpassword")
MSSQL_HOST = os.getenv("MSSQL_HOST", "127.0.0.1")
MSSQL_DB   = os.getenv("MSSQL_DB", "master")
MSSQL_PORT = os.getenv("MSSQL_PORT", "1433")

# NOTE: Untuk SQL Server 2000 biasanya butuh ODBC Driver lama
# contoh: "SQL Server" atau "FreeTDS"
CONN_STR = f"DRIVER={{FreeTDS}};SERVER={MSSQL_HOST};PORT={MSSQL_PORT};UID={MSSQL_USER};PWD={MSSQL_PASS};DATABASE={MSSQL_DB};TDS_Version=7.0"

@app.route("/health", methods=["GET"])
def health():
    try:
        conn = pyodbc.connect(CONN_STR, timeout=5)
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify({"status": "ok", "result": row[0]}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("APP_PORT", "8080")))
