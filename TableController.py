import sqlite3


class Table():
    """
    Class to manipulate with sql tables
    """

    connection = None
    cursor = None

    def connect_to_db(self):
        """
        Method to create and connect to DB
        If DB already exists it just connect to it.
        """
        try:
            self.connection = sqlite3.connect('test_database.db')
            self.cursor = sqlite3.connect('test_database.db').cursor()
            return self.connection, self.cursor
        except EnvironmentError:
            print(EnvironmentError)

    def create_table(self, name):
        """
        Create a table
        """
        # self.cursor = self.connection.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS {} (
                                        id integer PRIMARY KEY,
                                    path_to_source_data VARCHAR(255),
                                    path_to_result_file VARCHAR(255),
                                    size_of_result_file VARCHAR(255)
                                    ); """.format(name))

    def write_data_to_result_table(self, id_column, path_src,
                                   path_result, size_of_result_file):
        """
            id_column = id column in table
            path_src = path_to_source_data column
            path_result = path_to_result_file
            size_of_result_file the same column
        """
        self.cursor.execute("""INSERT INTO result_files
                            VALUES('1','2','3','4');""")
