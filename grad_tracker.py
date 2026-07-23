import json

class GradeTracker:
    """A class to track student grades."""

    def __init__(self):
        # Initialize an empty dictionary to store students and their grades.
        # try to load existiing data from students.json when the program starts.
        pass

    def add_student(self, name):
        # add a new student with an empty list of grades.
        pass

    def add_grade(self, name, grade):
        # add a grade to an existing student
        # handle the case where the student doesn't exist
        pass

    def get_average(self, name):
        # calculate and return the average grade for a student
        # handle the case where the student has no grades
        pass

    def display_all(self):
        # loop through all students and print their name and average grade
        pass

    def save_data(self):
        # save the students dictionary to students.json
        pass

    def load_data(self):
        # load data from students.json
        # handle the case where the file doesn't exist yet
        pass

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
            pass
        elif choice == '2':
            # get name and grade from user and call add_grade
            pass
        elif choice == '3':
            # call display all
            pass
        elif choice == '4':
            # get name from user and cal get_average
            pass
        elif choice == '5':
            # call save_data and break the loop
            pass
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()