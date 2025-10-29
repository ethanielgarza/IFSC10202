class Pet:
    # Attributes
    Name = ""
    Type = ""
    Age = 0

    # No-argument constructor
    def __init__(self):
        pass

    def set_name(self, name):
        self.Name = name

    def set_type(self, pet_type):
        self.Type = pet_type

    def set_age(self, age):
        self.Age = age

# Function to read file, create objects, and print attributes
def main():
    pets = []
    with open("10.01 Pets.txt", "r") as file:
            for line in file:
                data = line.strip().split(", ")
                if len(data) == 3:
                    pet = Pet()
                    pet.set_name(data[0])
                    pet.set_type(data[1])
                    pet.set_age(int(data[2]))
                    pets.append(pet)

    # Print the header
    print("{:<10} {:<10} {:<10}".format("Name", "Type", "Age"))

    # Print attributes of each pet object
    for pet in pets:
        print("{:<10} {:<10} {:<10}".format(pet.Name, pet.Type, pet.Age))

if __name__ == "__main__":
    main()




