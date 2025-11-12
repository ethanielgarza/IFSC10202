class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []  # Start empty; will add grades later

    def RunningAverage(self):
        non_zero = [g for g in self.Grades if g > 0]
        if not non_zero:
            return 0.0
        return sum(non_zero) / len(non_zero)

    def TotalAverage(self):
        """Average of all grades, treating blanks as zero."""
        if not self.Grades:
            return 0.0
        return sum(self.Grades) / len(self.Grades)

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


class StudentList:
    def __init__(self):
        self.StudentList = []

    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.StudentList.append(student)

    def find_student(self, tnumber):
        for i, student in enumerate(self.StudentList):
            if student.TNumber == tnumber:
                return i
        return -1

    def print_student_list(self):
        print(f"{'First Name':>12} {'Last Name':>12} {'ID Number':>12} {'Running Avg':>12} {'Semester Avg':>12} {'Letter':>12}")
        print("-" * 80)
        for student in self.StudentList:
            run_avg = student.RunningAverage()
            sem_avg = student.TotalAverage()
            letter = student.LetterGrade()
            print(f"{student.FirstName:>12} {student.LastName:>12} {student.TNumber:>12} {run_avg:>12.2f} {sem_avg:>12.2f} {letter:>12}")

    def add_student_from_file(self, filename):
        with open(filename, "r") as f:
            for line in f:
                if line.strip():
                    firstname, lastname, tnumber = line.strip().split(",")
                    self.add_student(firstname, lastname, tnumber)

    def add_scores_from_file(self, filename):
        with open(filename, "r") as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split(",")
                    tnumber = parts[0]
                    score = parts[1] if len(parts) > 1 else ""
                    index = self.find_student(tnumber)
                    if index != -1:
                        if score.strip() == "":
                            self.StudentList[index].Grades.append(0)
                        else:
                            self.StudentList[index].Grades.append(int(score))


def main():
    # Create the student list
    s_list = StudentList()

    # Step 1: Add students
    s_list.add_student_from_file("11.Project Students.txt")

    # Step 2: Add scores
    s_list.add_scores_from_file("11.Project Scores.txt")

    # Step 3: Print results
    s_list.print_student_list()


if __name__ == "__main__":
    main()
