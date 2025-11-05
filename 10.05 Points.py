# Step 1 - Define the class object "Point"
class Point:
# Step 2 - Define the initializer and any default values
    def __init__(self, Xvalue, Yvalue):
# Step 3 - Define the object attributes
        self.x = Xvalue
        self.y = Yvalue
# Step 4 - Define the methods for the object
# ToString returns a nicely formated string to represent the data point
    def ToString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

import math

def Distance(PointA, PointB):
    return math.sqrt((PointB.x - PointA.x)**2 + (PointB.y - PointA.y)**2)

def MidPoint(PointA, PointB):
    mid_x = (PointA.x + PointB.x) / 2
    mid_y = (PointA.y + PointB.y) / 2
    return Point(mid_x, mid_y)

def XAngle(PointA, PointB):
    if PointB.x - PointA.x == 0:
        return 90.0 if PointB.y > PointA.y else -90.0
    slope = (PointB.y - PointA.y) / (PointB.x - PointA.x)
    return math.degrees(math.atan(slope))

def main():
    with open("10.05 Points.txt", "r") as file:
        for line in file:
            values = line.strip().split(',')
            x1, y1, x2, y2 = map(float, values)
            
            pointA = Point(x1, y1)
            pointB = Point(x2, y2)
            
            distance = Distance(pointA, pointB)
            midpoint = MidPoint(pointA, pointB)
            xangle = XAngle(pointA, pointB)
            
            print("-" * 75)
            print(f"Point A: {pointA.ToString()}, Point B: {pointB.ToString()}, Distance: {distance:.7f}, Midpoint: {midpoint.ToString()}, Angle: {xangle:.7f}")

if __name__ == "__main__":
    main()