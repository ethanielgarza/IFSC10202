def ParseDegreeString(ddmmss_str):
    degree_symbol_pos = ddmmss_str.find(chr(176))
    minute_symbol_pos = ddmmss_str.find("'")
    second_symbol_pos = ddmmss_str.find('"')
    
    degrees = float(ddmmss_str[:degree_symbol_pos])
    minutes = float(ddmmss_str[degree_symbol_pos+1:minute_symbol_pos])
    seconds = float(ddmmss_str[minute_symbol_pos+1:second_symbol_pos])
    
    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

def main():
    input_file_name = "07.Project Angles Input.txt"
    output_file_name = "07.Project Angles Output.txt"
    
    with open(input_file_name, 'r') as infile, open(output_file_name, 'w') as outfile:
            record_count = 0
            for line in infile:
                line = line.strip()
                if line:
                    degrees, minutes, seconds = ParseDegreeString(line)
                    decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
                    outfile.write(f"{decimal_degrees}\n")
                    record_count += 1
            
            print(f"{record_count} records processed")
            
if __name__ == "__main__":
    main()
