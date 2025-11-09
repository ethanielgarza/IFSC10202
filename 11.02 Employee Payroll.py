class Employee:
    def __init__(self, FirstName, LastName, IDNumber, Wage):
        self.FirstName = FirstName
        self.LastName = LastName
        self.IDNumber = IDNumber
        self.Wage = Wage
        self.HoursWorked = 0

    def WeeklyPay(self):
        if self.HoursWorked > 40:
            overtime_hours = self.HoursWorked - 40
            overtime_pay = overtime_hours * 1.5 * self.Wage
            regular_pay = 40 * self.Wage
            return regular_pay + overtime_pay
        else:
            return self.HoursWorked * self.Wage
def find_employee(employee_list, employee_id):
    for i, employee in enumerate(employee_list):
        if employee.IDNumber == employee_id:
            return i
    return -1
# Assuming the files 11.02 Employees.txt and 11.02 Hours.txt exist with the provided data

# Read employees from 11.02 Employees.txt
employees = []
with open("11.02 Employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(", ")
        first_name, last_name, id_number, wage = data
        employees.append(Employee(first_name, last_name, id_number, float(wage)))

# Read hours worked from 11.02 Hours.txt and update employees
with open("11.02 Hours.txt", "r") as f:
    for line in f:
        data = line.strip().split(", ")
        id_number, hours = data
        index = find_employee(employees, id_number)
        if index != -1:
            employees[index].HoursWorked = float(hours)

# Print the header
print(f"{'First Name':<12}{'Last Name':<12}{'ID Number':<12}{'Hours Worked':<15}{'Hourly Wage':<15}{'Weekly Pay':<12}")

# Print the results for each employee
for employee in employees:
    weekly_pay = employee.WeeklyPay()
    print(f"{employee.FirstName:<12}{employee.LastName:<12}{employee.IDNumber:<12}{employee.HoursWorked:<15.2f}{employee.Wage:<15.2f}{weekly_pay:<12.2f}")
