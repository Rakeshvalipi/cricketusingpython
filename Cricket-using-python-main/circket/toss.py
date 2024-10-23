import random
def toss():
# Toss
    toss_result = random.choice(["Heads", "Tails"])
    user_toss_choice = input("Choose heads or tails: ").capitalize()
    toss_winner = "User" if user_toss_choice == toss_result else "Computer"
    print(f"\nToss Result: {toss_result}")
    print(f"{toss_winner} won the toss")

    if toss_winner == "User":
          user_choice = input("Choose to bat or bowl: ").lower()
          computer_choice = "bowl" if user_choice == "bat" else "bat"
          print(f"user won the toss and chose to {user_choice} ")
          if user_choice=='bat':
               return 'user'
          else:
               return 'computer'

    else:
        computer_choice = random.choice(["bat", "bowl"])
        user_choice = "bowl" if computer_choice == "bat" else "bat"
        print(f"computer won the toss and chose to {computer_choice}")
        if computer_choice=='bat':
               return 'computer'
        else:
               return 'user'

