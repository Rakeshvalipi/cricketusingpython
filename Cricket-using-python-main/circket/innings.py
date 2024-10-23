import random
from choice import *
def play_innings1(player, overs, max_wickets):
    first_runs = 0
    wickets = 0
    balls = 0

    print(f"\n{player}'s Innings Begins")

    while wickets < max_wickets and balls < overs * 6:
        try:
            user_choice = get_user_choice()
            computer_choice = random.randint(1, 6)

            print(f"Your choice: {user_choice}\nComputer's choice: {computer_choice}")

            if user_choice == computer_choice:
                wickets += 1
            else:
                if user_choice > computer_choice:
                  first_runs +=computer_choice
                else:
                    first_runs +=user_choice

            if max_wickets==wickets:
                print("           -------ALL OUT-----")

            balls += 1

            if balls % 6 == 0:
                over_number = balls // 6
                print(f"End of Over {over_number}")
                print(
                    f"Over {over_number} Summary: {player} scored {first_runs} runs with {wickets} wickets."
                )

            print(f"Total Score: {first_runs}/{wickets}")
            print(f"Balls remaining: {overs * 6 - balls}")

        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

    print("\nEnd of Innings")
    print(f"Final Score for {player}:\nRuns = {first_runs}\nWickets = {wickets}")

    return first_runs, wickets



def play_innings2(player, overs, max_wickets,first_runs):
    runs = 0
    wickets = 0
    balls = 0

    print(f"\n{player}'s Innings Begins")

    while wickets < max_wickets and balls < overs * 6 and first_runs>=runs:
        try:
            user_choice = get_user_choice()
            computer_choice = random.randint(1, 6)

            print(f"Your choice: {user_choice}\nComputer's choice: {computer_choice}")

            if user_choice == computer_choice:
                wickets += 1
            else:
                if user_choice > computer_choice:
                  runs +=computer_choice
                else:
                    runs +=user_choice

            if max_wickets==wickets:
                print("ALL OUT")

            balls += 1

            if balls % 6 == 0:
                over_number = balls // 6
                print(f"End of Over {over_number}")
                print(
                    f"Over {over_number} Summary: {player} scored {runs} runs with {wickets} wickets."
                )

            print(f"Total Score: {runs}/{wickets}")
            print(f"Balls remaining: {overs * 6 - balls}")

        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

    print("\nEnd of Innings")
    print(f"Final Score for {player}:\nRuns = {runs}\nWickets = {wickets}")

    return runs, wickets