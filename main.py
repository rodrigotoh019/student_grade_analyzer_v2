# Main program
students = []
num_students = int(input('How many are the new Students:	'))  # Dictates how many set of data this program will have

# Name data collection
for i in range(1, num_students + 1):
    while True:
        name = input(f"Enter the name of Student #{i}:  ").strip().title()
        if not is_valid_name(name):
            print("Invalid name! Please avoid using special characters or numbers.")
            continue

        # Score data collection
        scores = []
        for n in range(1, 5):
            while True:
                try:
                    score = float(input(f'Score{n}:  '))
                    if 1 <= score <= 100:
                        scores.append(score)  # Formatting the scores value per name
                        break
                    else:
                        print('Please enter a score between 1 and 100.')
                except ValueError:
                    print('Invalid Input! Please enter a numeric value.')

        # Appending every data set to the main list
        students.append([name, scores])  # (['name'], [score1, score2, score3, score4])
        break