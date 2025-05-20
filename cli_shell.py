# CLI Shell - User interaction and menu routing

while True:
    prompt = input("Type 'Open' to access the menu and type 'Close' to quite:\n>").lower()

    if prompt == "open":
        break
    elif prompt == "close":
        exit()
    else:
        print("Invalid Input! Please choose between 'Open' or 'Close'.")

while True:
    print("\n=== Student Grade Analyzer Menu ===")
    print("1. View All Students")
    print("2. Add a Student")
    print("3. Edit a Student")
    print("4. Remove a Student")
    print("5. Analyze Scores")
    print("6. Exit")

    choice = input("Choose an option (1 - 6):\n>")

    if choice == "1":
        # view_student()
    elif choice == "2":
        # add_student()
    elif choice == "3":
        # edit_student()
    elif choice == "4":
        # remove_student()
    elif choice == "5":
        # analyze_score()
    elif choice == "6":
        print("Exiting The Program. Good bye!")
        break
    else:
        print("Invalid Option. Please select between 1 - 6.")