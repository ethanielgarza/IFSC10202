class Student:
    def __init__ (self, firstname, lastname, tnumber, scores):

        self.Firstname = firstname
        self.Lastname = lastname
        self.TNumber = tnumber
        self.Grades = [int(score) if score and str(score).strip() else 0 for score in scores]

    def  RunningAverage (self):
        non_zero_grades = [grade for grade in self.Grades if grade > 0]
        if not non_zero_grades:
            return 0.0
        return sum(non_zero_grades) / len(non_zero_grades)

    def TotalAverage (self):
        if not self.Grades: 
            return 0.0
        return sum(self.Grades) / len(self.Grades)

    def LetterGrade (self):
        total_average = self.TotalAverage()
        if total_average >= 90:
            return "A"
        elif total_average >= 80:
            return "B"
        elif total_average >= 70:
            return "C"
        elif total_average >= 60:
            return "D"
        else:
            return "F"

def main():
    with open("10.Project Student Scores.txt", "r") as file:
        print(f"{'First Name':<15}{'Last Name':<15}{'ID Number':<15}{'Running Average':<20}{'Semester Average':<20}{'Letter Grade':<15}")
        for line in file:
            data = line.strip().split(',')
            firstname, lastname, tnumber = data[0], data[1], data[2]
            scores = data [3:]
            student = Student(firstname, lastname, tnumber, scores)

            running_avg = student.RunningAverage()
            total_avg = student.TotalAverage()
            letter_grade = student.LetterGrade()

            print("-"* 98)
            print(f"{student.Firstname:<15}{student.Lastname:<15}{student.TNumber:<15}{running_avg:<20}{total_avg:<20}{letter_grade:<15}")
       
if __name__ == "__main__":
    main()