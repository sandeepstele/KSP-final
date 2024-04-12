import os

def rename_files(directory):
    # Iterate over files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file name contains an underscore
        if '_' in filename:
            # Split the file name by underscore
            parts = filename.split('_')
            # Remove the portion after the first underscore
            new_filename = parts[0] + os.path.splitext(filename)[1]
            # Construct the new file path
            new_filepath = os.path.join(directory, new_filename)
            old_filepath = os.path.join(directory, filename)
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"File '{filename}' renamed to '{new_filename}'")

# Provide the directory containing the files to be renamed
directory = '2/District/'
rename_files(directory)
