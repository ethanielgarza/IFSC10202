# Define Class
class Student:
    # Define Initializer and Parameters 
    def __init__(self, firstname, lastname, tnumber, scores):
        # Deifine Attributes
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        # Convert all scores to integers, handling empty strings as None
        self.scores = [int(score) if score else None for score in scores]
# Define Methods for the Object
    def RunningAverage(self):
        # Calculate the average of non-blank scores
        valid_scores = [score for score in self.scores if score is not None]
        if not valid_scores:
            return 0.0
        return sum(valid_scores) / len(valid_scores)

    def TotalAverage(self):
        # Calculate the average of all scores, treating missing scores as 0
        total = 0
        count = len(self.scores)
        if count == 0:
            return 0.0
        for score in self.scores:
            if score is not None:
                total += score
        return total / count

    def LetterGrade(self):
        average = self.TotalAverage()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
# Main program fucntion 
def main():

    print("First Name Last Name ID Number Running Average Semester Average Letter Grade")
 
 # This reads from the '10.Project Student Scores.txt' file.
    with open("10.Project Student Scores.txt", 'r') as file:
         for line in file:
            # Split the line by comma and remove any leading/trailing whitespace
            parts = [part.strip() for part in line.split(',')]
            
            firstname, lastname, tnumber = parts[0], parts[1], parts[2]
            scores = parts[3:]

            student = Student(firstname, lastname, tnumber, scores)

            running_avg = student.RunningAverage()
            total_avg = student.TotalAverage()
            letter_grade = student.LetterGrade()

            print(f"{firstname:<11}{lastname:<12}{tnumber:<12}{running_avg:<17.2f}{total_avg:<19.2f}{letter_grade:<12}")


if __name__ == "__main__":
    main



