# Student Grade Analyzer v2

This is an updated version of the Student Grade Analyzer (SGA) project by Rodrigo Toh, designed to be more modular, readable, and future-proof. This update focuses on breaking down the core `analyze_scores` function into helper sub-functions, returning structured data for cleaner logic, and preparing for the next stage — Command Line Interface (CLI) interaction.

## ✅ What's New (as of May 25, 2025)

### 🧠 Modular Function Design

The `analyze_scores()` function has been split into the following sub-functions for better reusability and debugging:

- `get_score_grade_average()` — Computes the overall average score and grade.
- `get_highest_lowest_scores()` — Finds the highest and lowest scoring students.
- `get_passed_failed_students()` — Separates passed and failed students and counts failures. Now returns a dictionary for clarity.
- `sort_students_by_name()` — Sorts the student list alphabetically by name.

### 🧼 Clean Main Function

The updated `analyze_scores()` now uses unpacking and organized variable assignments to prepare a `result` dictionary for all student insights.

```python
def analyze_scores(students_data):
    avg_score, avg_grade = get_score_grade_average(students_data)
    highest, lowest = get_highest_lowest_scores(students_data)
    pass_fail_data = get_passed_failed_students(students_data)
    passed = pass_fail_data["passed"]
    failed = pass_fail_data["failed"]
    fail_count = pass_fail_data["fail_count"]
    sorted_students = sort_students_by_name(students_data)

    result = {
        'average_score': avg_score,
        'grade_average': avg_grade,
        'highest': highest,
        'lowest': lowest,
        'passed': passed,
        'failed': failed,
        'fail_count': fail_count,
        'sorted_students': sorted_students,
    }
    return result
```

## 📁 File Structure (Planned)

- `main.py` — Main CLI entry point (coming next).
- `utils.py` — Contains all helper functions.
- `README.md` — You are here.

## 🔜 Next Step

- Begin implementing the CLI interface to interact with the system via user input and options.
- Provide users with the ability to add, edit, remove, and analyze student records directly from the terminal.

---

Project maintained by [Rodrigo Toh](https://github.com/rodrigotoh019)
