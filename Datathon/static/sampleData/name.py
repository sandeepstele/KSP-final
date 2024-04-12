import os

def extract_and_write_text(folder_path, output_file):
    with open(output_file, 'w') as f:
        files = os.listdir(folder_path)
        for file_name in files:
            text_after_dash = file_name.split('.')[0] # Extract text after '-'
            f.write(text_after_dash + '\n')  # Write text to file

# Specify the folder path containing the files
folder_path = '2/District/'

# Specify the output file path
output_file = '2/output6.txt'

# Call the function to extract text and write to file
extract_and_write_text(folder_path, output_file)
