def FahrToCel(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp - 32) * 5 / 9
    return celsius_temp
input_file_name = "06.03 FTemps.txt"
output_file_name = "06.03 CTemps.txt"
records_processed = 0
with open(input_file_name, 'r') as infile, open(output_file_name, 'w') as outfile:
    for line in infile:
        fahrenheit = float(line.strip())
        celsius = FahrToCel(fahrenheit)
        outfile.write(f"{celsius:5.1f}\n")
        records_processed += 1
print(f"{records_processed} records written")