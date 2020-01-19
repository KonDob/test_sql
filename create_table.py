#!/usr/bin/env python3
import os
import sys
import sqlite3
from CSV_Agent import CSVAgent
import Folder_controller
import TableController

PATH_TO_CVS = os.path.join('Default_data_for_test_task/data.csv')
csv = CSVAgent(PATH_TO_CVS)
fc = Folder_controller.Folder()

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
# Find record id data.csv by ID
fc.create_folder('result_data')
result_data = csv.find_record_by_id()

# Copiyng ID folder with content to parent folder
fc.copy_folder(result_data)