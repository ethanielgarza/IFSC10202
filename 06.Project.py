input_filename = "06.Project Input File.txt"
merge_filename = "06.Project Merge File.txt"
output_filename = "06.Project Output File.txt"

input_records = 0
merge_records = 0
output_records = 0

with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    for line in infile:
        if "**Insert Merge File Here**" in line:
            with open(merge_filename, 'r') as mergefile:
                for merge_line in mergefile:
                    merge_records += 1
                    output_records += 1
                    outfile.write(merge_line);
            outfile.write("\n")
        else:
            output_records += 1
            input_records += 1
            outfile.write(line);
print(f"{input_records} input file records")
print(f"{merge_records} merge file records")
print(f"{output_records} output file records")