import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE")
        )
        print("Successfully connected to the database.")
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to the MySQL database: {err}")
        print("Please check your database settings and ensure the MySQL server is running.")
        exit(1)
