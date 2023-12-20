
# Database Schema & Relationships Export

## Description
This Python script is designed to connect to a MySQL database, extract schema information, and display this data in both the console and a text file. It's particularly useful for database analysis and documentation purposes. The script gathers details about each table in the database, such as table names, column names, primary key status, foreign key references, and uniqueness constraints.

## Features
- Extracts detailed schema information from a MySQL database.
- Outputs the schema information to the console.
- Writes the schema information to a text file for documentation purposes.
- Handles sensitive database connection details securely using environment variables.

## Prerequisites
- Python installed on your machine.
- MySQL database accessible with proper credentials.
- Python packages: `mysql.connector` and `dotenv`.

## Installation
1. Ensure Python is installed on your machine.
2. Install the required Python packages:

   ```sh
   pip install mysql-connector-python python-dotenv
   ```

3. Clone or download this script to your local machine.

## Usage
1. If running the script for the first time, it will prompt you to enter your database connection details (host, user, password, database name). These details will be saved in a `.env` file.
2. Run the script using Python:

```
python script_name.py
```

3. The script will connect to your database, extract the schema information, and display it in the console as well as write it to a file named `db_schema_output.txt`.

## Contributing
Contributions to enhance the functionality of this script are welcome. Feel free to fork the repository, make your changes, and create a pull request.

## Contact
Charl Cronje
Email: charl.cronje@mail.com
Project Link: [https://github.com/charlpcronje/Combine-Markdown-Docs.git](https://github.com/charlpcronje/Combine-Markdown-Docs.git)

## License
This project is open-source and available under the MIT License.

