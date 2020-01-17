import os
import CSV_Agent

csv = CSV_Agent()



class Folder():
    folder_name = 'asdf'
    PATH_FOR_FOLDER = os.path.join()

    def create_folder(path):
        os.mkdir(path)