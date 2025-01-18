import os
import psycopg2

db_host = os.getenv("DB_HOST", "db")
db_user = os.getenv("DB_USER", "postgres")
db_password = os.getenv("DB_PASSWORD", "secret")
db_name = os.getenv("DB_NAME", "testdb")

def check_db_connection():
    conn = psycopg2.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        dbname=db_name
    )
    conn.close()

if __name__ == "__main__":
    print("WEB: Attempting DB connection ...")
    try:
        check_db_connection()
        print("WEB: Successfully connected to the database!")
    except Exception as e:
        print("WEB: Failed to connect to the database:", e)