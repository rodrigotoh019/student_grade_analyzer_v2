# Special Characters Exemption
import re

def is_valid_name(name):
    return bool(re.match(r"^[A-Za-zÑñ' -]+$", name))


# Letter grade bracket
def letter_grade_scale(student_score):
    if student_score >= 97:
        return 'A+'
    elif student_score >= 93:
        return 'A'
    elif student_score >= 90:
        return 'A-'
    elif student_score >= 87:
        return 'B+'
    elif student_score >= 83:
        return 'B'
    elif student_score >= 80:
        return 'B-'
    elif student_score >= 77:
        return 'C+'
    elif student_score >= 73:
        return 'C'
    elif student_score >= 70:
        return 'C-'
    elif student_score >= 67:
        return 'D+'
    elif student_score >= 63:
        return 'D'
    elif student_score >= 60:
        return 'D-'
    else:
        return 'F'


# Individual data mapping and formatting
def individual_scores(student_data):
    result = []
    for name, scores in student_data:
        student_avg = round(sum(scores) / len(scores), 2)
        student_dict = {
            'name': name,
            'scores': scores,
            'grades': [letter_grade_scale(score) for score in scores],
            'average': student_avg,
            'average_grade': letter_grade_scale(student_avg)
        }
        result.append(student_dict)
    return result

def get_score_grade_average(students_data):
    all_score = [score for _, scores in students_data for score in scores]
    student_avg = round(sum(all_score) / len(all_score))
    grade_average = letter_grade_scale(student_avg)
    return student_avg, grade_average

def get_highest_lowest_scores(students_data):
    highest = max(students_data, key=lambda x: sum(x[1]) / len(x[1]))
    lowest = min(students_data, key=lambda x: sum(x[1])/len(x[1]))
    return highest, lowest

def get_passed_failed_students(students_data):
    failed = []
    passed = []
    for name, scores in students_data:
        student_avg = sum(scores) / len(scores)
        if student_avg < 60:
            failed.append((name, scores))
        else:
            passed.append((name, scores))
    fail_count = len(failed)
    return {
        'passed': passed,
        'failed': failed,
        'fail_count': fail_count
    }

def sort_students_by_name(students_data):
    sorted_students = sorted(students_data, key=lambda x: x[0])
    return sorted_students

# Analysis utility - computes highest, lowest, average, and categorizes pass/fail students
def analyze_scores(students_data):
    avg_score, ave_grade = get_score_grade_average(students_data)
    highest, lowest = get_highest_lowest_scores(students_data)
    pass_fail_data = get_passed_failed_students(students_data)
    passed = pass_fail_data["passed"]
    failed = pass_fail_data["failed"]
    fail_count = pass_fail_data["fail_count"]
    sorted_students = sort_students_by_name(students_data)

    result = {
        'average_score': avg_score,
        'grade_average': ave_grade,
        'highest': highest,
        'lowest': lowest,
        'passed': passed,
        'failed': failed,
        'fail_count': fail_count,
        'sorted_students': sorted_students,
    }
    return result

# Process and output results
results = analyze_scores(students)

print("\n--- Analysis Summary ---")
print(f"Average Score: {results['average']}")
print(f"Average Grade: {results['grade_average']}")
print(f"Highest Scorer: {results['highest'][0]} - {results['highest'][1]}")
print(f"Lowest Scorer: {results['lowest'][0]} - {results['lowest'][1]}")
print(f"Passed Students ({len(results['passed'])}): {results['passed']}")
print(f"Failed Students ({results['fail_count']}): {results['failed']}")