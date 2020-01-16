import sqlite3


class Table:
    """
    Class to manipulate with sql tables
    """
    connection = None

def connect_to_db():
    """
    Method to create and connect to DB
    If DB already exists it just connect to it.
    """
    connection = None
    try:
        connection = sqlite3.connect('test_database.db')
        return connection
    except:
        print(Error)

def create_table():
    """
    Create a table
    """
    cursor.execute(""" CREATE TABLE IF NOT EXISTS result_files (
                                        id integer PRIMARY KEY,
                                        path_to_source text NOT NULL,
                                        path_to_result_file text NOT NULL,
                                        size_of_result_file text NOT NULL
                                    ); """)

connection = connect_to_db()
cursor = connection.cursor()