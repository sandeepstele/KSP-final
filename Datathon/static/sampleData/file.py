import os
folder_path = 'duplicated_maps/'
files = os.listdir(folder_path)
file_names = [file_name for file_name in files if file_name.endswith('.html')]
print(file_names)