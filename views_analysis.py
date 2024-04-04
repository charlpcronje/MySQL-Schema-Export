import mysql.connector
import os  # Importing the os module
from database_connection import connect_to_db
from markdown_writer import write_table_data_to_markdown

def get_views(cursor):
    cursor.execute("""
        SELECT 
            VIEW_NAME, 
            TABLE_NAME 
        FROM 
            INFORMATION_SCHEMA.VIEW_TABLE_USAGE
        WHERE 
            VIEW_SCHEMA = %s
        ORDER BY 
            VIEW_NAME;
    """, (os.getenv("DB_DATABASE"),))
    views = cursor.fetchall()
    view_details = {}
    for view_name, table_name in views:
        if view_name not in view_details:
            view_details[view_name] = set()
        view_details[view_name].add(table_name)
    return view_details

def format_view_data(view_data):
    formatted_data = []
    for view_name, tables in view_data.items():
        formatted_view = [f"<details>\n<summary>{view_name}</summary>\n"]
        for table_name in tables:
            formatted_view.append(f"  - Uses table `{table_name}`")
        formatted_view.append("</details>\n")
        formatted_data.append('\n'.join(formatted_view))
    return '\n'.join(formatted_data)

def write_views_to_markdown(view_data, filename):
    formatted_data = format_view_data(view_data)
    with open(filename, 'a') as file:
        file.write("\n## Database Views\n\n")
        file.write(formatted_data)

def main():
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        view_data = get_views(cursor)
        filename = 'MySQL Database Schema.md'  # You can change the filename as needed
        write_views_to_markdown(view_data, filename)
    finally:
        cursor.close()
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
