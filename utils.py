# Special Characters Exemption
import re

def is_valid_name(name):
    return bool(re.match(r"^[A-Za-zÑñ' -]+$", name))

# Letter grade bracket
def letter_grade_scale(student_score):
    if student_score >= 90:
        return 'A'
    elif student_score >= 80:
        return 'B'
    elif student_score >= 70:
        return 'C'
    elif student_score >= 60:
        return 'D'
    else:
        return 'F'

# Individual data mapping and formatting
def individual_scores(student_data):
    result = []
    for name, scores in student_data:
        grades = [letter_grade_scale(score) for score in scores]
        average = round(sum(scores) / len(scores), 2)
        average_grade = letter_grade_scale(average)

        student_dict = {
            'name': name,
            'scores': scores,
            'grades': grades,
            'average': average,
            'average_grade': average_grade
        }

        result.append(student_dict)

    return result


# Analysis utility - computes highest, lowest, average, and categorizes pass/fail students
def analyze_scores(students_data):
    all_score = [score for _, scores in students_data for score in scores]
    average = round(sum(all_score) / len(all_score), 2)
    grade_average = letter_grade_scale(average)

    highest = max(students_data, key=lambda x: sum(x[1])/len(x[1]))
    lowest = min(students_data, key=lambda x: sum(x[1])/len(x[1]))

    failed = [(name, scores) for name, scores in students_data if sum(scores)/len(scores) <= 60]
    passed = [(name, scores) for name, scores in students_data if sum(scores)/len(scores) > 60]

    fail_count = len(failed)
    sort_asc = sorted(students_data, key=lambda x: x[0])

    result = {
        'highest': highest,
        'lowest': lowest,
        'average': average,
        'grade_average': grade_average,
        'passed': passed,
        'failed': failed,
        'fail_count': fail_count,
        'sorted': sort_asc,
    }
    return result

students = [['Rod', [88, 90, 29, 39]], ['Bibi', [90, 80, 22.19]]]



# Process and output results
results = analyze_scores(students)

# print("\n--- Analysis Summary ---")
# print(f"Highest Scorer: {results['highest'][0]} - {results['highest'][1]}")
# print(f"Lowest Scorer: {results['lowest'][0]} - {results['lowest'][1]}")
# print(f"Average Score: {results['average']}")
# print(f"Passed Students ({len(results['passed'])}): {results['passed']}")
# print(f"Failed Students ({results['fail_count']}): {results['failed']}")