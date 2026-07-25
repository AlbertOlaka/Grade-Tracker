import json

class GradeTracker:
    """A class to track student grades."""

    def __init__(self):
        # Initialize an empty dictionary to store students and their grades.
        # try to load existiing data from students.json when the program starts.
        self.students = {}
        self.load_data()

    def load_data(self):
            # load data from students.json
            # handle the case where the file doesn't exist yet
            try:
                with open('students.json', 'r') as f:
                    self.students = json.load(f)
            except FileNotFoundError:
                self.students = {}

    def add_student(self, name):
        # add a new student with an empty list of grades.
        if name not in self.students:
            self.students[name] = []
        else:
            print(f"{name} already exists.")

    def add_grade(self, name, grade):
        # add a grade to an existing student
        # handle the case where the student doesn't exist
        try:
            self.students[name].append(grade)
        except KeyError:
            print(f"{name} not found. Add them first.")

    def get_average(self, name):
        # calculate and return the average grade for a student
        # handle the case where the student has no grades
        grades = self.students.get(name, [])
        if not grades:
            print(f"{name} has no grades yet.")
            return None
        return sum(grades) / len(grades)

    def display_all(self):
        # loop through all students and print their name and average grade
        if not self.students:
            print("No students yet.")
            return
        for name, grades in self.students.items():
            avg = self.get_average(name)
            if avg is not None:
                print(f"{name}: {avg:.2f}")
            else:
                print(f"{name}: no grades yet")

    def save_data(self):
        # save the students dictionary to students.json
        with open('students.json', 'w') as f:
            json.dump(self.students, f)

    

def main():
    tracker = GradeTracker()

    while True:
        print("\n--- Grade Tracker ---")
        print("1. Add student")
        print("2. Add grade")
        print("3. View all students")
        print("4. Get student average")
        print("5. Save and quit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            # get name from user and call add_student
            name = input("Student name: ")
            tracker.add_student(name)
        elif choice == '2':
            # get name and grade from user and call add_grade
            name = input("Student name: ")
            grade_input = input("Grade: ")
            try:
                grade = float(grade_input)
                tracker.add_grade(name, grade)
            except ValueError:
                print("That's not a valid number.")
        elif choice == '3':
            # call display all
            tracker.display_all()
        elif choice == '4':
            # get name from user and cal get_average
            name = input("Student name: ")
            avg = tracker.get_average(name)
            if avg is not None:
                print(f"{name}'s average: {avg:.2f}")
        elif choice == '5':
            # call save_data and break the loop
            tracker.save_data()
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()