def remove_duplicates(input_file, output_file):
    unique_lines = set()

    # Read input file and store unique lines in a set
    with open(input_file, 'r') as f:
        for line in f:
            unique_lines.add(line.strip())

    # Write unique lines to output file
    with open(output_file, 'w') as f:
        for line in unique_lines:
            f.write(line + '\n')

# Specify the input file path
input_file = '2/output8.txt'

# Specify the output file path
output_file = '2/profession1.txt'

# Call the function to remove duplicates
remove_duplicates(input_file, output_file)
