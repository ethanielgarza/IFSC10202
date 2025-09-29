def merge_files(input_file, merge_file, output_file):
    # Initialize counters
    input_count = 0
    merge_count = 0
    output_count = 0

    # Open the files
    with open(input_file, 'r') as infile, open(merge_file, 'r') as mergefile, open(output_file, 'w') as outfile:
        # Iterate through each line of the input file
        for line in infile:
            input_count += 1
            output_count += 1
            
            # Write the line to the output file
            outfile.write(line)

            # Check if the line contains the merge placeholder
            if "**Insert Merge File Here**" in line:
                # Copy lines from the merge file
                for merge_line in mergefile:
                    merge_count += 1
                    output_count += 1
                    outfile.write(merge_line)
        
        # Write the remaining lines from the input file if any
        for remaining_line in infile:
            input_count += 1
            output_count += 1
            outfile.write(remaining_line)
    
    # Print the counts of records
    print(f"{input_count} input file records")
    print(f"{merge_count} merge files records ")
    print(f"{output_count} output file records")

# File names
input_file = '06.Project Input File.txt'
merge_file = '06.Project Merge File.txt'
output_file = '06.Project Output File.txt'

# Call the function to merge files
merge_files(input_file, merge_file, output_file)