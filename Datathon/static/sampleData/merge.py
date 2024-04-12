import csv

def merge_text_files(file1_path, file2_path, output_csv_path):
    # Read contents of the first text file
    with open(file1_path, 'r') as file1:
        content1 = file1.readlines()
    
    # Read contents of the second text file
    with open(file2_path, 'r') as file2:
        content2 = file2.readlines()
    
    # Merge the contents line by line
    merged_content = [f"{line1.strip()},{line2.strip()}\n" for line1, line2 in zip(content1, content2)]
    
    # Write the merged content into a CSV file without quoting
    with open(output_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE, escapechar=' ')
        for line in merged_content:
            writer.writerow(line.split(','))

# Example usage:
file1_path = '2/output3.txt'
file2_path = '2/output4.txt'
output_csv_path = 'merged_file.csv'
merge_text_files(file1_path, file2_path, output_csv_path)
