import os

def extract_and_write_text(folder_path, output_file):
    with open(output_file, 'w') as f:
        files = os.listdir(folder_path)
        for file_name in files:
            if '-' in file_name:
                if(file_name.endswith('.html')):
                    file_names, extension = os.path.splitext(file_name)
                    text_after_dash = file_names.split('-')[0] # Extract text after '-'
                    f.write(text_after_dash + '\n')  # Write text to file

# Specify the folder path containing the files
folder_path = '2/3/'

# Specify the output file path
output_file = '2/output4.txt'

# Call the function to extract text and write to file
extract_and_write_text(folder_path, output_file)
