import random
def co_choose():
 comp_choice=["rock","paper","scissors"]
 return random.choice(comp_choice)
def us_choice():
 user_choice=input("Enter your choice (rock/paper/scissors):").lower()
 if user_choice in ["rock", "paper", "scissors"]:
  return user_choice 
 else :
  print("invalid input")
def winner():
 user_choice=us_choice()
 computer_choice=co_choose()
 print(f"Computer choosed {computer_choice}")
 if user_choice == computer_choice:
    print("It's a tie!")
    return "tie"
 elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
    return "win"
 else:
    print("You lose!")
    return "lose"
u=0
c=0 
choice=input("start the game (yes/no)")
while choice=="yes":
 w=winner()
 if w=="win":
   u+=1
 elif w=="lose":
   c+=1
 print(f"Scores Are")
 print(f"Comp={c}")
 print(f"User={u}")
 choice=input("do you want to play more(yes/no)")    
  