properties = []
with open("Exam Two Properties.csv", "r") as file:
    lines = file.readlines()
for line in lines:
    data = line.strip().split(',')
    data[4] = float(data[4])
    properties.append(data)
headings = ["Address", "City", "State", "Zipcode", "Price"]
print(f"{headings[0]:<30}{headings[1]:<20}{headings[2]:<10}{headings[3]:<15}{headings[4]:<15}")
for row in properties:
    print(f"{row[0]:<30}{row[1]:<20}{row[2]:<10}{row[3]:<15}{row[4]:<15}")

zipcodes = []
for property_entry in properties:
    zip_code = property_entry[3]
    price = property_entry[4]
    found = False
    for zipcode_entry in zipcodes:
        if zipcode_entry[0] == zip_code:
            zipcode_entry[1] += 1
            zipcode_entry[2] += price
            found = True
            break
    if not found:
        zipcodes.append([zip_code, 1, price])

print("Zipcode    Count    Average")

for zipcode_entry in zipcodes:
    zip_code = zipcode_entry[0]
    count = zipcode_entry[1]
    total_price = zipcode_entry[2]

    average_price = total_price / count
    print(f"{zip_code:^10}  {count:<5}    ${average_price:,.2f}")
