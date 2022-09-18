import os 
import shutil

class Clean:
    def __init__(self, fileExtention, fileFolder):
        self.fileExtention = fileExtention;
        self.fileFolder = fileFolder;

    def arrange(self):
        for files in os.listdir('.'):
            if files.endswith(self.fileExtention):
                if os.path.exists(self.fileFolder) == True:

                    shutil.move(files, self.fileFolder)
                else:
                    os.mkdir(self.fileFolder)
                    shutil.move(files, self.fileFolder)
            else:
                pass

