import re

def generate_index_for_schema_file(schema_file_path, index_file_path):
    # Regular expression to match <summary> line following <details>
    summary_regex = re.compile(r'\s*<summary>(.+)</summary>')

    index = {}
    current_section = None
    in_details_block = False
    start_line = None

    with open(schema_file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            if '<details>' in line:
                in_details_block = True
                start_line = line_number
                continue

            if '</details>' in line and in_details_block:
                in_details_block = False
                if current_section and current_detail:
                    # Adjusting the format to match the new structure
                    index[current_section][current_detail] = [start_line, line_number]
                continue

            if in_details_block:
                summary_match = summary_regex.match(line)
                if summary_match:
                    current_detail = summary_match.group(1).strip()
                    if current_section not in index:
                        index[current_section] = {}
                    continue

            section_match = re.match(r'##\s+(.+)', line)
            if section_match:
                current_section = section_match.group(1)
                # Adjusting to match the section title format in the new structure
                current_section = current_section
                index[current_section] = {}

    # Writing to YAML file with new format
    with open(index_file_path, 'w') as file:
        file.write("---\n")
        file.write("Title: MySQL Database Schema Index\n")
        file.write("Description: Index for `ig_db` database used by `Ignite` application. Each item references a location in \"MySQL Database Schema.md\" here the first number represents the start line number and the second number represents the end line number.\n")
        for section, details in index.items():
            file.write(f"{section}:\n")
            for detail, lines in details.items():
                file.write(f"  {detail}: {lines}\n")
        file.write("---")

generate_index_for_schema_file('MySQL Database Schema.md', 'MySQL Database Schema Index.yml')
