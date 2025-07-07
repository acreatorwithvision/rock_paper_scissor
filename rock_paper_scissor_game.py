""" 
1. get the input from the user - rock, paper, scissor
2. let the computer choose a random one - rock, paper, scissor
3. print result

Cases 
A. Rock
1. rock - rock =tie
2. rock - paper=paper win
3. rock - scissor = rock win

B. Paper
1. paper - rock = paper wins
2. paper - paper = tie
3. paper - scissor = scissor wins

C. Scissor
1. scissor - rock = rock wins
2. scissor - paper = scissor wins
3. scissor - scissor = tie
"""


import random
item_list = ["Rock","Paper","Scissor"]


user_choice=input("Enter your move = Rock , Paper , Scissor\n")
comp_choice=random.choice(item_list)


print(f"User choice = {user_choice}, Computer choice = {comp_choice}")


if user_choice == comp_choice:
    print("Both chooses same: Match Tied")

elif user_choice == "Rock" and comp_choice == "Rock":
    print("Both chooses same: Match Tied")

elif user_choice == "Paper" and comp_choice == "Paper":
    print("Both chooses same: Match Tied")

elif user_choice == "Scissor" and comp_choice == "Scissor":
    print("Both chooses same: Match Tied") 

elif user_choice == "Rock" and comp_choice == "Paper":
    print("Rock - Paper, Computer wins")

elif user_choice == "Rock" and comp_choice == "Scissor":
    print("Rock - Scissor, User wins")

elif user_choice == "Paper" and comp_choice == "Rock":
    print("Paper - Rock, User wins")

elif user_choice == "Paper" and comp_choice == "Scissor":
    print("Paper - Scissor, Computer wins")

elif user_choice == "Scissor" and comp_choice == "Rock":
    print("Scissor - Rock, Computer wins")

elif user_choice == "Scissor" and comp_choice == "Paper":
    print("Scissor - Paper, User wins")

else:
    print("Wrong Arguement")