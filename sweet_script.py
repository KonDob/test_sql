#!/usr/bin/env python3
import os
from CSV_Agent import CSVAgent
import Folder_controller
from TableController import Table

PATH_TO_CVS = os.path.join('Default_data_for_test_task/data.csv')
csv = CSVAgent(PATH_TO_CVS)
fc = Folder_controller.Folder()
db = Table()

# Create DB
db.connect_to_db()

# Create Table result_files()
db.create_table('result_files')

# Write data to table
db.write_data_to_result_table(1, "fsfd", "asdf", "asdf")
