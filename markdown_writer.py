import os
import re

def format_relationship(column_name, ref_table, ref_column, is_primary, ref_is_unique):
    if not ref_table:
        return column_name
    if is_primary == 1 and ref_is_unique == 1:
        return f"{column_name} <--> {ref_table}.{ref_column}"
    elif is_primary == 1:
        return f"{column_name} <-->> {ref_table}.{ref_column}"
    elif ref_is_unique == 1:
        return f"{column_name} <<--> {ref_table}.{ref_column}"
    else:
        return f"{column_name} <<-->> {ref_table}.{ref_column}"

def write_table_data_to_markdown(data, filename):
    with open(filename, 'w') as file:
        file.write("# MySQL Database Schema\n\n")
        file.write("This file outlines the schema of a MySQL database, detailing all tables, columns, and their relationships. The relationships are depicted using symbols to represent the type and direction of connections between tables, based on foreign keys.\n\n")
        
        file.write("### Relationship Symbols:\n")
        file.write("- `<<-->>`: Many-to-Many Relationship. Multiple records in one table are associated with multiple records in another, typically via a junction table.\n")
        file.write("- `<<-->`: One-to-Many Relationship (One on the right). A single record in the right table can be associated with multiple records in the left table.\n")
        file.write("- `<-->>`: One-to-Many Relationship (One on the left). A single record in the left table can be associated with multiple records in the right table.\n")
        file.write("- `<-->`: One-to-One Relationship. A record in one table is associated with only one record in another table.\n\n")
        file.write("### Primary Key Indication:\n")
        file.write("- `#` : If a column name starts with a `#` it means that it is the primary key of the table.\n\n")
        file.write(f"## MySQL Table Schema for Database: {os.getenv('DB_DATABASE')}\n\n")

        unique_foreign_keys = set()
        current_table = None
        for row in data:
            table, column, is_primary, ref_table, ref_column, is_unique, ref_is_unique, constraint_name = row
            if table != current_table:
                if current_table is not None:
                    file.write("\n</details>\n\n")
                file.write(f"<details>\n<summary>{table}</summary>\n\n")
                current_table = table
            
            column_display = f"- {'#' if is_primary else ''}{column}"
            if ref_table and constraint_name:
                fk_identifier = f"{table}.{column}.{constraint_name}"
                if fk_identifier not in unique_foreign_keys:
                    unique_foreign_keys.add(fk_identifier)
                    column_display += f" <<--> {ref_table}.{ref_column} (FK: {constraint_name})"
            file.write(f"  {column_display}\n")
        file.write("\n</details>\n")

        # Writing the count of unique foreign keys at the end of the document
        file.write(f"\n - Total Unique Foreign Keys: {len(unique_foreign_keys)}\n\n\n")

def write_stored_procedures_to_markdown(categorized_procs, filename):
    with open(filename, 'a') as file:
        file.write(f"## MySQL Stored Procedure Categories for Database: {os.getenv('DB_DATABASE')}\n\n")
        file.write("This section categorizes stored procedures based on their inferred functionality from their names...\n\n")

        for category, procs in categorized_procs.items():
            file.write(f"<details>\n<summary>{category}</summary>\n\n")
            for proc in procs:
                parts = re.findall(r'[a-z]+|[A-Z]+(?![a-z])|[A-Z][a-z]*', proc)
                proc_description = ' '.join(part if part.isupper() else part.capitalize() for part in parts)
                file.write(f"- {proc} ({proc_description})\n")
            file.write("\n</details>\n\n")
