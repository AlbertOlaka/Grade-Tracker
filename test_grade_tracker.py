from grad_tracker import GradeTracker

def test_add_student():
    """Test that a student is added correctly."""
    tracker = GradeTracker()
    tracker.students = {}

    tracker.add_student('Lucy')

    assert 'Lucy' in tracker.students
    assert tracker.students['Lucy'] == []

def test_add_grade():
    """Test that a grade is added to an existing student."""
    tracker = GradeTracker()
    tracker.students = {}

    tracker.add_student('Lucy')
    tracker.add_grade('Lucy', 90)

    assert tracker.students['Lucy'] == [90]

def test_get_average():
    """Test that the average is calculated correctly."""
    tracker = GradeTracker()
    tracker.students = {}

    tracker.add_student('Lucy')
    tracker.add_grade('Lucy', 80)
    tracker.add_grade('Lucy', 100)

    assert tracker.get_average('Lucy') == 90.0