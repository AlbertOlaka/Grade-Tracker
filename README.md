# Grade Tracker

A command-line application for tracking student grades, calculating averages, 
and persisting data across sessions.

---

## Problem It Solves

Teachers and tutors managing student grades manually through spreadsheets 
or paper records have no programmatic way to calculate averages, detect 
missing grades, or maintain a persistent record across sessions. This tool 
provides a simple, reliable CLI interface for managing that data.

---

## Features

- Add students to a tracker
- Record multiple grades per student
- Calculate individual student grade averages
- Persist data across sessions using JSON storage
- Handles invalid input gracefully without crashing

---

## Tech Stack

- Python 3.13.7
- JSON for data persistence
- pytest for testing

---

## Project Structure
grade_tracker/
│
├── grade_tracker.py 
├── test_grade_tracker.py 
├── students.json 
|── README.md 

---

## How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/grade-tracker.git
cd grade-tracker
```

**2. Run the application:**
```bash
python grade_tracker.py
```

**3. Run the tests:**
```bash
pytest test_grade_tracker.py
```

---

## How to Use

When you run the program you'll see a menu:
--- Grade Tracker ---

1. Add student
2. Add grade
3. View all students
4. Get student average
5. Save and quit

- Choose **1** to add a new student by name
- Choose **2** to record a grade for an existing student
- Choose **3** to view all students and their current averages
- Choose **4** to get the average for a specific student
- Choose **5** to save all data and exit

Data is automatically saved to `students.json` when you choose option 5 
and reloaded the next time you run the program.

---

## What I Learned

- How to structure a Python project using classes and separation of concerns
- File handling and JSON serialization for data persistence
- Exception handling for FileNotFoundError and ValueError
- Writing pytest tests for class methods
- The difference between printing and returning values in Python functions

---

## What I Would Improve

- Add the ability to delete students or remove individual grades
- Add a search function to find students by name
- Export grade reports to CSV
- Add grade letter classification — A, B, C, D, F based on score ranges
- Replace JSON storage with a proper SQLite database

---

## Author

Albert Joseph  
