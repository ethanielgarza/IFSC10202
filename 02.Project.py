print("Great Circle Calculator")
radius = float(input("Enter Radius of Sphere: "))
point1 = float(input("Starting Point - Enter Latitude: "))
point2 = float(input("Starting Point - Enter Longitude: "))
end1 = float(input("Ending point - Enter Latitude: "))
end2 = float(input("Ending Point - Enter Longitude: "))

import math
# instead of using the formula for finding the cos and sin in radians lat1 = (point1 * pi) + (point1 / 180)
# short hand that helps shorten code = math.radians

lat1 = math.radians(point1)
long1 = math.radians(point2)
lat2 = math.radians(end1)
long2 = math.radians(end2)

dif1 = long2 - long1
dif2 = lat2 - lat1

a = math.sin(dif2 / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dif1 / 2)**2
c = 2 * math.asin(math.sqrt(a))
distance = radius * c 

number = distance
roundnumber = round(number, 2)
print('The Great Circle Distance:', roundnumber)