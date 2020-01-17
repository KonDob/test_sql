import pandas as pd
import os
import csv
import sys

class CSVAgent():

    id_input = int(sys.argv[1])

    """
    Class to manipulate and manage data
    from CSV format files
    """
    def __init__(self,filepath):
        self.csv_file = pd.read_csv(filepath, engine='c')

    def find_record_by_id(self,id_input=id_input):
        try:
            return self.csv_file[self.csv_file.id == id_input].name[0]
        except IndexError as e:
            print("Name with id = {} not found".format(id_input))
