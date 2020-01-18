import os


class Folder():
    folder_name = 'asdf'
    # PATH_FOR_FOLDER = os.path.join()

    def create_folder(self,name):
        path = str(os.path.split(os.getcwd())[0])
        folder_path = path + '/{}'.format(name)
        try:
            os.mkdir(folder_path)
        except OSError as e:
            print('Directory already exists')
