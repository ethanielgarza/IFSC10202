class Employee:
    
    def __init__ (self, employeenumber, firstname, lastname, address, city, state, zip):

        # Attributes
        self.EmployeeNumber = employeenumber
        self.Firstname = firstname
        self.Lastname = lastname
        self.Address = address
        self.City = city
        self.State = state
        self.Zip = zip

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
                    emp = Employee(
                        int(parts[0]), parts[1], parts[2],parts[3], parts[4], parts[5], parts[6])
                    self.employees.append(emp)
   
    def WriteEmployeeFile (self):
        with open (self.filename, 'w') as file:
            for e in self.employees:
                file.write(f"{e.employeenumber}, {e.firstname}, {e.lastname}"
                           f"{e.address}, {e.city}, {e.state}, {e.zip}\n")
                
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
        
    def ReadEmployee (self, employeenumber):
        index = self.FindEmployee(employeenumber)
        if index == -1:
            return None
        e = self.employees[index]
        return (e.employeenumber, e.firstname, e.lastname, e.address, e.state, e.zip)
    
    def NextEmployeeNumber (self):
        if not self.employees:
            return 1
        return self.employees[-1].employeenumber + 1

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
    