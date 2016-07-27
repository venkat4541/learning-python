import os

def rename_files():
    #Get files names from the folder
    file_list = os.listdir(r"E:\GitHub\python\learning-python\alphabet")
    os.chdir(r"E:\GitHub\python\learning-python\alphabet")
    #For each file, rename the file name
    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")
        os.rename(file_name,new_name)
        print(file_name+" changed to "+new_name)

rename_files()
