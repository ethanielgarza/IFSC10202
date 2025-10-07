import sys

def ParseDegreeString(ddmmss):
    """
    Parses a string in the format DD°MM'SS" and returns the degrees, minutes, and seconds as floating-point numbers.
    """
    try:
        # Find the degree symbol
        degree_symbol_pos = ddmmss.find(chr(176))
        degrees = float(ddmmss[:degree_symbol_pos])

        # Find the minutes symbol
        minutes_symbol_pos = ddmmss.find("'")
        minutes = float(ddmmss[degree_symbol_pos+1:minutes_symbol_pos])

        # Find the seconds symbol
        seconds_symbol_pos = ddmmss.find('"')
        seconds = float(ddmmss[minutes_symbol_pos+1:seconds_symbol_pos])

        return degrees, minutes, seconds
    except (ValueError, IndexError):
        # Handle cases where the format is not as expected
        return None, None, None

def DDMMSStoDecimal(degrees, minutes, seconds):
    """
    Converts degrees, minutes, and seconds to a single decimal degree value.
    """
    if degrees is None or minutes is None or seconds is None:
        return None
    
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

def main():
    """
    Main function to read a file, convert angles, and write to an output file.
    """
    input_file = "07.Project Angles Input.txt"
    output_file = "07.Project Angles Output.txt"

    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            lines = f_in.readlines()
            records_processed = 0

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                degrees, minutes, seconds = ParseDegreeString(line)
                if degrees is not None:
                    decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
                    if decimal_degrees is not None:
                        f_out.write(f"{decimal_degrees}\n")
                        records_processed += 1
            
            print(f"{records_processed} records processed")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
