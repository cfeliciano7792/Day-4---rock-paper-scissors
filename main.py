rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

user_choice = int(choice)

pc_choice = random.randint(0,2)


if user_choice == 0 and pc_choice == 1:
  print(f"{rock}\nComputer chose:\n{scissors}\nYou win")

elif user_choice == 0 and pc_choice == 2:
  print(f"{rock}\nComputer chose:\n{paper}\nYou lose")

elif user_choice == 0 and pc_choice == 0:
  print(f"{rock}\nComputer chose:\n{rock}\nTie Game")

elif user_choice == 1 and pc_choice == 0:
  print(f"{paper}\nComputer chose:\n{rock}\nYou Win")

elif user_choice == 1 and pc_choice == 1:
  print(f"{paper}\nComputer chose:\n{paper}\nTie Game")

elif user_choice == 1 and pc_choice == 2:
  print(f"{paper}\nComputer chose:\n{scissors}\nYou Lose")

elif user_choice == 2 and pc_choice == 0:
  print(f"{scissors}\nComputer chose:\n{rock}\nYou Lose")

elif user_choice == 2 and pc_choice == 1:
  print(f"{scissors}\nComputer chose:\n{paper}\nYou Win") 

elif user_choice == 2 and pc_choice == 2:
  print(f"{scissors}\nComputer chose:\n{scissors}\nTie Game")


    
