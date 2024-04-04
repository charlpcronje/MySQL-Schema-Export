import os

def write_env_file(host, user, password, database):
    with open('.env', 'w') as file:
        file.write(f"DB_HOST={host}\n")
        file.write(f"DB_USER={user}\n")
        file.write(f"DB_PASSWORD={password}\n")
        file.write(f"DB_DATABASE={database}\n")

def prompt_for_db_details():
    print("Database connection details not found. Please enter the following details:")
    host = input("Database Host: ")
    user = input("Database User: ")
    password = input("Database Password: ")
    database = input("Database Name: ")
    write_env_file(host, user, password, database)
