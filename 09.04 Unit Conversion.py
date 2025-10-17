# Step 1: Read the conversion file into a 2D list
# Assuming '09.04 Conversion.txt' is in the same directory and contains tab-separated values.
with open("09.04 Conversion.txt", "r") as f:
    conversion_table = [line.strip().split() for line in f]

# Step 2: Get user input and validate units
try:
    from_value = float(input("Enter From Value: "))
except ValueError:
    print("FromValue must be a number")
    exit()

from_unit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
to_unit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")

from_index = -1
to_index = -1

# Search for the FromUnit
for i in range(len(conversion_table)):
    if conversion_table[i][0] == from_unit:
        from_index = i
        break

if from_index == -1:
    print("FromUnit is not valid")
    exit()

# Search for the ToUnit
for i in range(len(conversion_table[0])):
    if conversion_table[0][i] == to_unit:
        to_index = i
        break

if to_index == -1:
    print("ToUnit is not valid")
    exit()

# Step 3: Perform the conversion and display the result
multiplier = float(conversion_table[from_index][to_index])
result = round(from_value * multiplier, 7)

print(f"{from_value:.1f} {from_unit} => {result} {to_unit}")
