# Student Grade Analyzer v2 (SGA v2)

SGA v2 is a Python-based CLI tool designed to help educators or users manage and analyze student grades across multiple grading periods. This version features a more robust structure, letter grading system, improved input validation, and an extendable architecture.

---

## ✅ Current Features (as of v2 Progress)

### 🔢 1. Multiple Scores Per Student (Per Quarter)
Each student has 4 scores:
- 1st Quarter
- 2nd Quarter
- 3rd Quarter
- 4th Quarter

### 🧮 2. Average Score Per Student
Each student’s average is automatically calculated from the 4 quarterly scores.

### 🔠 3. Letter Grading System
Each score and average is converted into a letter grade:
- A: 90–100
- B: 80–89
- C: 70–79
- D: 60–69
- F: 59 and below

### 🧼 4. Name Validation
Accepts names containing:
- Letters (A–Z, a–z)
- Spaces
- Apostrophes (e.g., O'Connor)
- Tilde-N (Ñ/ñ)

### 🧠 5. Robust Input Validation
- Accepts only numeric scores between **1 and 100**
- Handles invalid input types and out-of-range values gracefully

### 🖥️ 6. CLI Menu System (Shell-Style)
User-friendly CLI menu allows users to:
- Add a student
- Edit student data *(Coming soon)*
- Remove a student *(Coming soon)*
- View all student records *(Coming soon)*
- Analyze class scores (average, top, bottom, pass/fail breakdown)
- Exit the program

### 🗂️ 7. Organized Codebase
Code is modularized into three parts:
- `main.py` – Data collection entry point
- `cli_shell.py` – CLI-based interface for interaction
- `utils.py` – Contains helper functions for grading and analysis

### 📊 8. Analytics Features
The `analyze_scores()` function provides:
- Class average and its letter grade
- Highest and lowest scoring students
- Sorted list of students by name
- Pass/Fail count breakdown

---

## 🔧 Planned Features (In Progress)
- Full implementation of View, Edit, Remove functions in CLI
- Sorting options (by name, average score)
- Save/load data (file persistence)
- GUI/Web version
- More grading rubrics

---

## 📁 Sample File Structure

```
sga_project/
│
├── main.py          # Collects student input
├── cli_shell.py     # CLI interaction with menu
├── utils.py         # Grade analysis, validation, formatting
└── README.md        # Documentation file
```

---

## 🧠 Example Output Summary (via `analyze_scores()`)
```python
Highest Scorer: Bibi - [90, 80, 22.19]
Lowest Scorer: Rod - [88, 90, 29, 39]
Average Score: 61.24
Grade Average: D
Passed Students: [('Bibi', [90, 80, 22.19])]
Failed Students (1): [('Rod', [88, 90, 29, 39])]
```

---

## 👨‍💻 Author
**Rodrigo Toh** – Freelance Python Developer & AI/ML Student  
GitHub: [rodrigotoh019](https://github.com/rodrigotoh019)
