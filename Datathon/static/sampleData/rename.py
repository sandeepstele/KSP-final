import os

def rename_files(folder_path):
    files = os.listdir(folder_path)
    for file_name in files:
        if '-' in file_name:
            new_file_name =file_name.split('_')[0]
            #file_name.replace('-', '').replace(' ', '')
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
            print(f"Renamed {file_name} to {new_file_name}")

# Specify the folder path containing the files
folder_path = '2/Crime_group/'

# Call the function to rename files
rename_files(folder_path)
