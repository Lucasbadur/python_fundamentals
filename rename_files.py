import os

def rename_files():
    file_list = os.listdir(r"C:\Users\Lucas\Desktop\prank\prank")
    #print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Lucas\Desktop\prank\prank")

    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
                  
    os.chdir(saved_path)

rename_files()
