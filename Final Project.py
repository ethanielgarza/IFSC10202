class Employee:
    
    def __init__ (self, employeenumber, firstname, lastname, address, city, state, zip):

        # Attributes
        self.employeenumber = employeenumber
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

        # Validation Process and Checking Data to see any incorrections
        if not (isinstance(employeenumber, int)):
            raise ValueError ("Employee Number must be a Number")
        
        if not firstname:
            raise ValueError ("First Name is Required")
        
        if not lastname:
            raise ValueError ("Last Name is Required")
        
        if not address:
            raise ValueError ("Address is Required")
        
        if not city: 
            raise ValueError ("City is Required")
        
        if not (isinstance(state, str) and len(state) == 2 and state.isupper()):
            raise ValueError ("State must be two Capital Letters")
        
        if not (zip.isdigit() and len(zip) == 5):
            raise ValueError ("Zip Code must be 5 numeric digits")
        
class EmployeeList:
    
    def __init__ (self, filename):
        # Attributes
        self.filename = filename
        self.employees = []

    # Methods
    def ReadEmployeeFile (self):
        with open(self.filename, "r") as file:
            for line in file:
                parts = [p.strip() for p in line.split(",")]
                if len(parts) == 7:
                    emp = Employee(int(parts[0]), parts[1], parts[2],parts[3], parts[4], parts[5], parts[6])
                    self.employees.append(emp)
   
    def WriteEmployeeFile (self):
        with open (self.filename, 'w') as file:
            for e in self.employees:
                file.write(f"{e.employeenumber}, {e.firstname}, {e.lastname}, {e.address}, {e.city}, {e.state}, {e.zip}\n")
                
    def DisplayEmployeeList (self):

        print()

        print(f"{'Employee':<15}{'First':<15}{'Last':<15}{'Address':<15}{'City':<15}{'State':<10}{'Zip':<10}")
        print(f"{'Number':<15}{'Name':<15}{'Name':<15}")
        print("-" * 100)

        for e in self.employees:
            print(f"{e.employeenumber:<15}{e.firstname:<15}{e.lastname:<15}{e.address:<15}{e.city:<15}{e.state:<10}{e.zip:<10}")

            print()
    
    def FindEmployee(self,employeenumber):
        for i, e in enumerate(self.employees):
            if e.employeenumber == employeenumber:
                return i
        return -1 
        
    def ReadEmployee(self, employeenumber):
        index = self.FindEmployee(employeenumber)
        if index == -1:
            return None
        e = self.employees[index]
        return (e.employeenumber, e.firstname, e.lastname, e.address, e.city, e.state, e.zip)
    
    def NextEmployeeNumber (self):
        if not self.employees:
            return 1
        return max(e.employeenumber for e in self.employees) + 1

    def AddEmployee (self, first, last, addr, city, state, zip):
        emp_num = self.NextEmployeeNumber()
        emp = Employee(emp_num, first, last, addr, city, state, zip)
        self.employees.append(emp)

    def UpdateEmployee (self, employeenumber, first, last, addr, city, state, zip):
        index = self.FindEmployee(employeenumber)
        if index == -1:
            return False
        
        self.employees[index].firstname = first
        self.employees[index].lastname = last
        self.employees[index].address = addr
        self.employees[index].city = city
        self.employees[index].state = state
        self.employees[index].zip = zip

        return True
    
    def DeleteEmployee (self, employeenumber):
        index = self.FindEmployee(employeenumber)
        if index == -1:
            return False
        del self.employees[index]
        return True

def main():
    emp_list = EmployeeList("Final Project Employees.txt")
    emp_list.ReadEmployeeFile()

    while True:

        print()

        print("(A)dd a New Employee")
        print("(D)elete an Existing Employee")
        print("(C)hange an Existing Employee")
        print("(P)rint All Employees")
        print("(S)ave Changes to File")
        print("(Q)uit")
        selection = input("\n Enter Selection: ").upper()

        if selection == "A":
            first = input ("Enter First Name: ")
            last = input ("Enter Last Name: ")
            addr = input ("Enter Address: ")
            city = input ("Enter City: ")
            state = input ("Enter State: ").upper()
            zip = input ("Enter Zip Code: ")

            try:
                emp_list.AddEmployee(first, last, addr, city, state, zip)
                print ("Employee Added\n")
            except Exception as e:
                print("Error:", e, "\n")

        elif selection == "D":
            num = int(input("Enter Employee Number: "))
            if emp_list.DeleteEmployee(num):
                print("Deleted Employee\n")
            else:
                print("Error: Employee Not Found.\n")

        elif selection == "C":
            num = int(input("Enter Employee Number: "))
            index = emp_list.FindEmployee(num) 

            if index == -1:
                print("Employee Not Found.\n")
                continue
            while True:
                print("\n(F)irst Name")
                print("(L)ast Name")
                print("(A)ddress")
                print("(C)ity")
                print("(S)tate")
                print("(Z)ip")
                print("(B)ack To Main Menu")
                change = input("\nEnter Selection: ").upper()

                e = emp_list.employees[index]

                if change == "F":
                    e.firstname = input("Enter First Name: ")

                elif change == "L":
                    e.lastname = input("Enter Last Name: ")

                elif change == "A":
                    e.address = input("Enter Address: ")

                elif change == "C":
                    e.city = input("Enter City: ")

                elif change == "S":
                    s = input("Enter State: ").upper()
                    if len(s) == 2 and s.isupper():
                        e.state = s
                    else:
                        print("Invalid State.")

                elif change == "Z":
                    z = input("Enter Zip: ")
                    if z.isdigit() and len(z) == 5:
                        e.zip = z
                    else:
                        print ("Invalid Zip.")

                elif change == "B":
                    break

        elif selection == "P":
            emp_list.DisplayEmployeeList()
        
        elif selection == "S":
            emp_list.WriteEmployeeFile()
            print("File Saved\n")

        elif selection == "Q":
            print("Good-Bye")
            break

        else: 
            print ("Invalid Selection\n")

if __name__ == "__main__":
    main()
