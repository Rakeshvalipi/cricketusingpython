import random
from rules import *
from toss import *
from innings import *


rules()
res_toss=toss()

if res_toss=='user':
    play='user'
    play2='computer'
else:
    play='computer'
    play2='user'



overs=int(input("Enter the number of overs:"))
max_wickets=int(input("Enter the maximum number of wickets:"))

first_runs,first_wickets = play_innings1(play, overs,max_wickets)
second_runs,second_wickets = play_innings2(play2, overs, max_wickets,first_runs)

print("\n~~~~~~~~~~ Result ~~~~~~~~~~")
print(f"{play} total runs: {first_runs}")
print(f"{play2} total runs: {second_runs}")

if first_runs > second_runs:
    print(f"Congratulations! {play} won the Match by {first_runs - second_runs} runs.")
elif first_runs < second_runs:
    print(f"Better luck next time! The {play2} won the Match by {first_wickets- second_wickets} wicket.")
elif first_runs==second_runs:
    print("Scores are same")
else:
    print("Match is cancelled due to bad conditions")