#!/usr/bin/env python3
import os
import sys
import sqlite3
from CSV_Agent import CSVAgent
import Folder_controller
from TableController import Table

PATH_TO_CVS = os.path.join('Default_data_for_test_task/data.csv')
csv = CSVAgent(PATH_TO_CVS)
fc = Folder_controller.Folder()
db = Table()

#Create DB
db.connect_to_db()

#Create Table result_files()
db.create_table('result_files')

#Write data to table
db.write_data_to_result_table(1,"fsfd","asdf","asdf")
# Find record id data.csv by ID
# fc.create_folder('result_data')
# result_data = csv.find_record_by_id()

# Copiyng ID folder with content to parent folder
# fc.copy_folder(result_data)