# main.py
# Purpose: Main script to extract database schema, write to Markdown, and generate YAML index

from database_connection import connect_to_db
from env_file_handler import prompt_for_db_details
from schema_extraction import get_table_column_data, get_stored_procedures
from procedure_analysis import categorize_and_describe_stored_procedures
from markdown_writer import write_table_data_to_markdown, write_stored_procedures_to_markdown
from generate_index import generate_index_for_schema_file  # Importing the new function
import os

if not os.path.isfile('.env'):
    prompt_for_db_details()

conn = connect_to_db()
cursor = conn.cursor()

try:
    data = get_table_column_data(cursor)
    filename = 'MySQL Database Schema.md'

    write_table_data_to_markdown(data, filename)

    proc_list = get_stored_procedures(cursor)
    categorized_procs = categorize_and_describe_stored_procedures(proc_list)
    write_stored_procedures_to_markdown(categorized_procs, filename)

    # Append contents of 'MySQL View Analysis.md' to 'MySQL Database Schema.md'
    view_analysis_file = 'MySQL View Analysis.md'
    if os.path.exists(view_analysis_file):
        with open(view_analysis_file, 'r') as view_file:
            view_contents = view_file.read()
        with open(filename, 'a') as schema_file:
            schema_file.write("\n\n")
            schema_file.write(view_contents)

    # Generate YAML index after the Markdown file is saved
    generate_index_for_schema_file(filename, 'MySQL Database Schema Index.yml')

finally:
    cursor.close()
    conn.close()
    print("Database connection closed.")
