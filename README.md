# 📘 Student Grade Analyzer (SGA v2)

## 🧠 Project Overview

**SGA v2** is a command-line interface (CLI) Python program designed to help users collect and analyze student grades over four academic quarters. It builds upon earlier versions by introducing modularity, structured data collection, and a clear roadmap for future enhancements.

---

## ✅ Current Features

- Prompts for the number of students to be added.
- Collects:
  - Validated **student names** (alphabetic only, no numbers or special characters).
  - **Four quarterly scores** (validated for numeric range between 1–100).
- Stores each student record as:
  ```python
  ['Student Name', [score1, score2, score3, score4]]
  ```
- Contains utility function `is_valid_name()` for input sanitization.
- Initial implementation of `analyze_scores()` to determine:
  - Highest and lowest scores
  - Average score
  - Passed and failed students (based on a threshold)
  - Sorted list of students

---

## 🧩 File Structure

```
📦SGA-v2/
 ┣ 📄 main.py        # Main program logic for student input and validation
 ┣ 📄 utils.py       # Utilities: name validation and score analysis
 ┣ 📄 cli_shell.py   # CLI shell: menu and user navigation logic
 ┗ 📄 README.md      # Project overview and development roadmap
```

---

## 🚧 Upcoming Features

### 🔹 1. Average Score Per Student
Each student’s average will be computed from the 4 scores.

### 🔹 2. Letter Grading System
A–F grading will be implemented both per score and for overall average:
```
A = 90–100
B = 80–89
C = 75–79
D = 70–74
F = Below 70
```

### 🔹 3. Data Structure Update
Students will be stored in this format for deeper analysis:
```python
['Name', [score1, score2, score3, score4], average, letter_grade]
```

### 🔹 4. Enhanced CLI Features
- Add / Edit / Remove students
- Display all current records
- Trigger full analysis from CLI

### 🔹 5. File Saving and Loading (Planned v3)
- Save student records to a file
- Load data from existing files

### 🔹 6. Search and Filter (Planned v3)
- Filter by pass/fail
- Search by name or letter grade

---

## 👨‍💻 Author

Developed by **Rodrigo Toh** as a part of his Python learning journey toward AI/ML development. The project is intentionally structured and built step-by-step for clarity, modularity, and hands-on learning.

---

> *“Built line-by-line, learned the same way.”*