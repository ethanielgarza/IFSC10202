print("Great Circle Calculator")
radius = float(input("Enter Radius of Sphere: "))
point1 = float(input("Starting Point - Enter Latitude: "))
point2 = float(input("Starting Point - Enter Longitude: "))
end1 = float(input("Ending point - Enter Latitude: "))
end2 = float(input("Ending Point - Enter Longitude: "))

import math
degrees1 = math.radians(point1)
degrees2 = math.radians(point2)
degrees3 = math.radians(end1)
degrees4 = math.radians(end2)

dif1 = degrees4 - degrees2
dif2 = degrees3 - degrees1

a = math.sin(dif2 / 2)**2 + math.cos(degrees1) * math.cos(degrees3) * math.sin(dif1 / 2)**2
c = 2 * math.asin(math.sqrt(a))
distance = radius * c 

print("The Great Circle Distance:", distance )
