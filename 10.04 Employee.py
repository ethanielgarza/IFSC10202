class Employee:

    def __init__ (self, firstname, lastname, Idnumber, hoursworked, wage):
        
        self.Firstname = firstname
        self.Lastname = lastname
        self.IDNumber = Idnumber
        self.HoursWorked = float(hoursworked)
        self.Wage = float(wage)
    def Weeklypay (self):
        if self.HoursWorked <= 40:
            return self.HoursWorked * self.Wage
        else:
            return (40 * self.Wage) + ((self.HoursWorked - 40) * self.Wage * 1.5)

def main():
    print(f"{'First':<10}{'Last':<10}{'ID':<10}{'Hours':<10}{'Hourly':<10}{'Weekly':<10}")
    print(f"{'Name':<10}{'Name':<10}{'Number':<10}{'Worked':<10}{'Wage':<10}{'Pay':<10}")
    
    with open("10.04 Payroll.txt", "r") as file:
        for line in file:
            FirstName, LastName, IDNumber, HoursWorked, Wage = line.strip().split(', ')
            employee = Employee(FirstName, LastName, IDNumber, HoursWorked, Wage)
            weekly_pay = employee.Weeklypay()
            print(f"{employee.Firstname:<10}{employee.Lastname:<10}{employee.IDNumber:<10}{employee.HoursWorked:<10.2f}{employee.Wage:<10.2f}{weekly_pay:<10.2f}")

if __name__ == "__main__":
    main()