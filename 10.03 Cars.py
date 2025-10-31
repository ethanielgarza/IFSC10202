# Define class named car
class Car():
    # Define Initializer for class
    def __init__(self, Year, Make):
        #Define Attributes
        self.Year = Year
        self.Make = Make
        self.Speed = 0
        # Methods
    def Accelerate(self, value):
        self.Speed += value
    def Brake(self, value):
        self.Speed = max(0, self.Speed - value)
    with open("10.03 Cars.txt", "r") as file:
        lines = file.readlines()
#Read file and print output
with open("10.03 Cars.txt", "r") as file:
    lines = file.readlines()

first_line = lines[0].strip().split(", ")
year = int(first_line[0])
make = first_line[1]

my_car = Car(year, make)

print(f"Make: {my_car.Make}")
print(f"Year: {my_car.Year}")
print("Change\tSpeed")

for line in lines[1:]:
    change = int(line.strip())
    if change > 0:
        my_car.Accelerate(change)
    else:
        my_car.Brake(abs(change))
    print(f"{change}\t{my_car.Speed}")