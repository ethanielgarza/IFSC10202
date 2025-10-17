# Print the two-dimensional list as a verification step
for row in data:
    print(row)

from_city = input("Enter From City: ")
to_city = input("Enter To City: ")

from_city_found = False
from_index = -1
to_city_found = False
to_index = -1

for i in range(1, len(data)):
    if data [i][0] == to_city:
        from_index = i
        from_city_found = True
        break
for j in range(1, len(data[0])):
    if data[0][j] == to_city:
        to_index = j
        to_city_found = True
        break
if not from_city_found:
    print("Invalid From City")
elif not to_city_found:
    print("Invalid to City")
else:
    distance = data[from_index][to_index]
    print(f"{from_city} to {to_city} - {distance} miles")