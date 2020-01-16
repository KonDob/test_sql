import pandas as pd
import os

class CSVAgent():
    """
    Class to manipulate and manage data
    from CSV format files
    """
    PATH_TO_CSV=os.getcwd() + 'data.csv'

    def read_cvs(self,filepath, *args):
        pd.read_csv(filepath, *args)

    def find_record_by_id(self,ID_ARGUMENT):
        cursor.execute("""
        SELECT path_to_source
        FROM result_files
        WHERE id={}
        """.format(ID_ARGUMENT))
    pass