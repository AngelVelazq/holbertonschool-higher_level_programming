import MySQLdb

def list_states(username, password, database):
    """
    Lists all states from the database hbtn_0e_0_usa.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name

    Returns:
        None
    """
    db = None
    cursor = None
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object
        cursor = db.cursor()

        # SQL query to select all states
        query = "SELECT * FROM states ORDER BY id ASC"

        # Execute the query
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and database connection
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

if __name__ == "__main__":
    list_states("username", "password", "database")