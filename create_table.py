#!/usr/bin/env python3
import os
import sys
import sqlite3
import sys
from CSV_Agent import CSVAgent
import TableController
import pandas as pd



#print(glob.glob())
PATH_TO_CVS = os.getcwd() + '/Default_data_for_test_task/data.csv'
csv = CSVAgent(PATH_TO_CVS)

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
result_data = csv.find_record_by_id(PATH_TO_CVS)
# print(entity)
print(result_data)