# Special Characters Exemption

import re

def is_valid_name(name):
    return bool(re.match(r"^[A-Za-zÑñ' -]+$", name))


# Analysis utility - computes highest, lowest, average, and categorizes pass/fail students

def analyze_scores(students_data):
    lowest_score = min(students_data, key=lambda x: x[1])
    highest_score = max(students_data, key=lambda x: x[1])
    average = round(sum(score for _, score in students_data) / len(students_data), 2)
    passed = [(name, score) for name, score in students_data if score >= 70]
    failed = [(name, score) for name, score in students_data if score < 70]
    fail_count = len(failed)
    sort_asc = sorted(students_data, key=lambda x: x[0])

    result = {
        'highest': highest_score,
        'lowest': lowest_score,
        'average': average,
        'passed': passed,
        'failed': failed,
        'fail_count': fail_count,
        'Sorted': sort_asc
    }
    return result



# Process and output results
results = analyze_scores(students)

print("\n--- Analysis Summary ---")
print(f"Highest Scorer: {results['highest'][0]} - {results['highest'][1]}")
print(f"Lowest Scorer: {results['lowest'][0]} - {results['lowest'][1]}")
print(f"Average Score: {results['average']}")
print(f"Passed Students ({len(results['passed'])}): {results['passed']}")
print(f"Failed Students ({results['fail_count']}): {results['failed']}")