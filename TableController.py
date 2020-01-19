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


    def create_table(self,name):
        """
        Create a table
        """
        # self.cursor = self.connection.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS {} (
                                        id integer PRIMARY KEY,
                                        path_to_source text NOT NULL,
                                        path_to_result_file text NOT NULL,
                                        size_of_result_file text NOT NULL
                                    ); """.format(name))
    
    def write_data_to_table(self, table_name, *args):
        self.cursor.execute(
            """
            INSERT INTO {}({})
            VALUES()
            
            """.format(table_name,*args)
        )

    