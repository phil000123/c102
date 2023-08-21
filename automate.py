import os
import shutil

from_dir = "C:/Users/phil lin/Downloads"
todir = "C:/Users/phil lin/Downloads/test"

listoffiles = os.listdir(from_dir)
##print(listoffiles)
for fileName in listoffiles:
    name, extension = os.path.splitext(fileName)
##print(name)
    print(extension)
    if extension == '':
        continue
    if extension in ['.txt’, ‘.doc’, ‘.docx’, ‘.pdf’']:
        path = from_dir+'/'+fileName
        path2 = todir + '/' + "Image_Files"
        path3 = todir + '/' + "Image_Files" + '/' + fileName
        if os.path.exists(path2):
            shutil.move(path,path3)
        else:
            os.makedirs(path2)
            shutil.move(path,path3)
        