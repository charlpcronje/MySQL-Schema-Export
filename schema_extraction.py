import os

def get_table_column_data(cursor):
    query = """
    SELECT 
        t.table_name, 
        c.column_name, 
        IF((SELECT COUNT(*)
            FROM information_schema.table_constraints AS tc
            JOIN information_schema.key_column_usage AS kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
                AND tc.table_name = kcu.table_name
            WHERE tc.constraint_type = 'PRIMARY KEY'
                AND tc.table_schema = c.table_schema 
                AND tc.table_name = c.table_name 
                AND kcu.column_name = c.column_name) > 0, 1, 0) AS is_primary,
        k.referenced_table_name,
        k.referenced_column_name,
        COALESCE((SELECT COUNT(*)
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                    AND tc.table_schema = kcu.table_schema
                    AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'UNIQUE'
                    AND tc.table_schema = c.table_schema 
                    AND tc.table_name = c.table_name 
                    AND kcu.column_name = c.column_name), 0) AS is_unique,
        COALESCE((SELECT COUNT(*)
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                    AND tc.table_schema = kcu.table_schema
                    AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'UNIQUE'
                    AND tc.table_schema = k.referenced_table_schema 
                    AND tc.table_name = k.referenced_table_name 
                    AND kcu.column_name = k.referenced_column_name), 0) AS ref_is_unique,
        k.constraint_name
    FROM 
        information_schema.tables AS t
        JOIN information_schema.columns AS c ON t.table_schema = c.table_schema AND t.table_name = c.table_name
        LEFT JOIN information_schema.key_column_usage AS k ON c.table_schema = k.table_schema 
            AND c.table_name = k.table_name 
            AND c.column_name = k.column_name 
            AND k.referenced_table_schema IS NOT NULL
    WHERE 
        t.table_schema = %s AND
        t.table_type = 'BASE TABLE'  -- Add this line to filter out views
    ORDER BY 
        t.table_name, 
        c.ordinal_position;
    """
    cursor.execute(query, (os.getenv("DB_DATABASE"),))
    return cursor.fetchall()

def get_stored_procedures(cursor):
    cursor.execute("""
        SELECT ROUTINE_NAME
        FROM INFORMATION_SCHEMA.ROUTINES
        WHERE ROUTINE_SCHEMA = %s AND ROUTINE_TYPE = 'PROCEDURE';
    """, (os.getenv("DB_DATABASE"),))
    return [row[0] for row in cursor.fetchall()]
