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
                        int(parts[0]), parts[1], parts[2],
                        parts[3], parts[4], parts[5], parts[6]
                    )
                    self.employees.append(emp)
                    