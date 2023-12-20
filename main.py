import os
import mysql.connector
from dotenv import load_dotenv

# Function to write environment variables to a file
def write_env_file(host, user, password, database):
    with open('.env', 'w') as file:
        file.write(f"DB_HOST={host}\n")
        file.write(f"DB_USER={user}\n")
        file.write(f"DB_PASSWORD={password}\n")
        file.write(f"DB_DATABASE={database}\n")

# Function to prompt for database details
def prompt_for_db_details():
    print("Database connection details not found. Please enter the following details:")
    host = input("Database Host: ")
    user = input("Database User: ")
    password = input("Database Password: ")
    database = input("Database Name: ")
    write_env_file(host, user, password, database)

# Check if .env file exists and load it; otherwise, prompt for details
if not os.path.isfile('.env'):
    prompt_for_db_details()

# Load environment variables
load_dotenv()

# Function to connect to the database
def connect_to_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )

# Function to get table and column data from the database
def get_table_column_data(cursor):
    query = """
    SELECT 
        t.table_name, 
        c.column_name, 
        IF(k.column_name IS NOT NULL, 1, 0) AS is_primary,
        k.referenced_table_name,
        k.referenced_column_name,
        (SELECT COUNT(*) FROM information_schema.table_constraints tc
         JOIN information_schema.key_column_usage kcu ON tc.constraint_name = kcu.constraint_name
         WHERE tc.table_schema = c.table_schema AND tc.table_name = c.table_name AND tc.constraint_type = 'UNIQUE'
         AND kcu.column_name = c.column_name) AS is_unique,
        (SELECT COUNT(*) FROM information_schema.table_constraints tc
         JOIN information_schema.key_column_usage kcu ON tc.constraint_name = kcu.constraint_name
         WHERE tc.table_schema = k.referenced_table_schema AND tc.table_name = k.referenced_table_name AND tc.constraint_type = 'UNIQUE'
         AND kcu.column_name = k.referenced_column_name) AS ref_is_unique
    FROM 
        information_schema.tables t
        JOIN information_schema.columns c ON t.table_schema = c.table_schema AND t.table_name = c.table_name
        LEFT JOIN information_schema.key_column_usage k ON c.table_schema = k.table_schema 
            AND c.table_name = k.table_name 
            AND c.column_name = k.column_name 
            AND k.referenced_table_schema IS NOT NULL
    WHERE 
        t.table_schema = %s
    ORDER BY 
        t.table_name, 
        c.ordinal_position
    """
    cursor.execute(query, (os.getenv("DB_DATABASE"),))
    return cursor.fetchall()

# Function to format the relationship display
def format_relationship(column_name, ref_table, ref_column, is_unique, ref_is_unique):
    if not ref_table:
        return column_name

    if is_unique == 1 and ref_is_unique == 1:
        return f"{column_name} <--> {ref_table}.{ref_column}"
    elif is_unique == 1 or ref_is_unique == 1:
        return f"{column_name} <<--> {ref_table}.{ref_column}"
    else:
        # This would be a simplification, as identifying many-to-many requires detecting junction tables
        return f"{column_name} <<-->> {ref_table}.{ref_column}"

# Function to print and write table data
def print_and_write_table_data(data, file):
    current_table = None
    for row in data:
        table, column, is_primary, ref_table, ref_column, is_unique, ref_is_unique = row
        if table != current_table:
            if current_table is not None:
                print()
                file.write("\n")
            header = f"+ {table}"
            print(header)
            file.write(header + "\n")
            current_table = table
        column_display = f"- {'#' if is_primary else ''}{format_relationship(column, ref_table, ref_column, is_unique, ref_is_unique)}"
        print(f"  {column_display}")
        file.write(f"  {column_display}\n")

# Main script execution
conn = connect_to_db()
cursor = conn.cursor()

try:
    data = get_table_column_data(cursor)
    with open('schemaExported.txt', 'w') as file:
        print_and_write_table_data(data, file)
finally:
    cursor.close()
    conn.close()
