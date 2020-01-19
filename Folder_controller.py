import os
import shutil


class Folder():
 
    FOLDER_PATH = str(os.path.split(os.getcwd())[0])
 
    def create_folder(self, name):
        folder = self.FOLDER_PATH + '/{}'.format(name)
        try:
            os.mkdir(folder)
        except OSError:
            print('Directory {} already exists'.format(name))
    
    def copy_folder(self, name):
        src = os.getcwd() + '/Default_data_for_test_task/data_for_integration/{}'.format(name)
        dst = self.FOLDER_PATH + '/result_data/{}'.format(name)
        try:
            shutil.copytree(src,dst)
        except OSError:
            print('Directory with id = {} already exists'.format(name))
