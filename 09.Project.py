import io #Input and Output system that helps with running the program.
import csv #(comma separated value or "CSV_data")

# import CSV and also having it here so I can format correctly.
csv_data = """Cities,Boston,Buffalo,Chicago,Cleveland,Dallas,Denver,Detroit,El Paso,Houston
Boston,0,457,983,639,1815,1991,702,2358,1886
Buffalo,457,0,536,192,1387,1561,252,1928,1532
Chicago,983,536,0,344,931,1050,279,1439,1092
Cleveland,639,192,344,0,1205,1369,175,1746,1358
Dallas,1815,1387,931,1205,0,801,1167,625,242
Denver,1991,1561,1050,1369,801,0,1310,652,1032
Detroit,702,252,279,175,1167,1301,0,1696,1312
El Paso,2358,1928,1439,1746,625,652,1696,0,756
Houston,1886,1532,1092,1358,242,1032,1312,756,0"""

data_file = io.StringIO(csv_data) 
reader = csv.reader(data_file)
distances_list = list(reader)

# Print the two-dimensional list with proper spacing
for row in distances_list:
    print(' '.join(f'{item:<10}' for item in row))

from_city = input("Enter From City: ")
to_city = input("Enter To City: ")

# Find the indices for the from_city and to_city
from_index = -1
to_index = -1

for i, city_name in enumerate(distances_list[0]):
    if city_name == from_city:
        from_index = i
    if city_name == to_city:
        to_index = i

# Search the zeroth column for the from_city
for i, row in enumerate(distances_list):
    if row[0] == from_city:
        from_index = i
    if row[0] == to_city:
        to_index = i

# Check for invalid cities and print the result
if from_index == -1:
    print("Invalid From City")
elif to_index == -1:
    print("Invalid To City")
else:
    distance = distances_list[from_index][to_index]
    print(f"{from_city} to {to_city} - {distance} miles.")

