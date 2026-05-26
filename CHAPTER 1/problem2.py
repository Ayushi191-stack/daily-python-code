import os

#specify the directory you want to list the contents of
directory_path = '/newfolder'

#list all the files and directories in the specified directory
contents = os.listdir(directory_path)

#print each file and directory
for item in contents:
    print(item)