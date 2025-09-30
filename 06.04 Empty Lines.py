input_file_name = "06.04 EmptyLinesInput.txt"
output_file_name = "06.04 EmptyLinesOutput.txt"
lines_read = 0
lines_written = 0
with open(input_file_name, 'r') as infile, open(output_file_name, 'w') as outfile:
    for line in infile:
        lines_read += 1
        if line.strip():
            outfile.write(line)
            lines_written += 1
print(f"{lines_read} records read")
print(f"{lines_written} records written")