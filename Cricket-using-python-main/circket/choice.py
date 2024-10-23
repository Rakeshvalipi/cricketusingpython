def get_user_choice():
    while True:
        try:
            user_choice = int(input("Choose any number from 1 to 6: "))
            if 1 <= user_choice <= 6:
                return user_choice
            else:
                print("Please choose a number from 1 to 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")