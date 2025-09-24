def FahrToCel(fahrenheit_temp):
    celsius = (fahrenheit_temp - 32) * 5 / 9
    return celsius
def main():
    records_processed = 0
    try:
        with open("06.03 FTemps.txt","r") as ftemps_file, \
             open("06.03 FTemps.txt","w") as ctemps_file:
         for line in ftemps_file:
            fahrenheit_val = float(line)
            celsius_val = FahrToCel(fahrenheit_val)
            ctemps_file.write(f"{celsius_val:>5.1f}\n")
            records_processed += 1
    except FileNotFoundError:
        print("Error: One of the files was not found.")
        return
    except ValueError:
        print("Error: The input file contains non-numeric data.")
        return
    print(f"{records_processed} records written")
if __name__ == "__main__":
   main()


def FahrToCel(fahrenheit_temp):
    """
    Calculates the temperature in Celsius from a Fahrenheit temperature.
    
    Args:
        fahrenheit_temp (float): The temperature in Fahrenheit.
        
    Returns:
        float: The temperature in Celsius.
    """
    celsius = (fahrenheit_temp - 32) * 5 / 9
    return celsius

def main():
    """
    Main function to process temperatures from a file and write to another.
    """
    records_processed = 0
    
    try:
        # Open both files using 'with' statement for safe file handling.
        with open("06.03 FTemps.txt", "r") as ftemps_file, \
             open("06.03 CTemps.txt", "w") as ctemps_file:
            
            # Read and process each line from the input file.
            for line in ftemps_file:
                # Convert the line to a floating-point number.
                fahrenheit_val = float(line)
                
                # Calculate the Celsius temperature using the function.
                celsius_val = FahrToCel(fahrenheit_val)
                
                # Write the formatted Celsius temperature to the output file.
                # '{:.1f}'.format() rounds to one decimal, '>5' right-justifies to a width of 5.
                ctemps_file.write(f"{celsius_val:>5.1f}\n")
                
                records_processed += 1
                
    except FileNotFoundError:
        print("Error: One of the files was not found.")
        return
    except ValueError:
        print("Error: The input file contains non-numeric data.")
        return

    # Print the total number of records processed.
    print(f"Processed {records_processed} records.")

if __name__ == "__main__":
    main()



