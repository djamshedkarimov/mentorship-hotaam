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

# Write your code below this line 👇
import random

user_choice = input("what do you choose? Type 0 for rock, 1 for paper, or 2 for scissors\n")
computer_choice = random.randint(0, 2)

if user_choice == "0":
    # user choose rock
    print(f"you chose: rock\n{rock}")
    if computer_choice == 1:
        print(f"computer chose: paper\n{paper}\n")
        print("you lose")
    elif computer_choice == 2:
        print(f"computer chose: scissors\n{scissors}\n")
        print("you win")
    else:
        print(f"computer chose: rock\n{rock}\n")
        print("thats a draw")

elif user_choice == "1":
    # user chose paper
    print(f"you chose: paper\n{paper}")
    if computer_choice == 2:
        print(f"computer chose: scissors\n{scissors}\n")
        print("you lose")
    elif computer_choice == 0:
        print(f"computer chose: rock\n{rock}\n")
        print("you win")
    else:
        print(f"computer chose: paper\n{paper}\n")
        print("thats a draw")

else:
    # user chose scissors
    print(f"you chose: scissors\n{scissors}")
    if computer_choice == 0:
        print(f"computer chose: rock\n{rock}\n")
        print("you lose")
    elif computer_choice == 1:
        print(f"computer chose: paper\n{paper}\n")
        print("you win")
    else:
        print(f"computer chose: scissors\n{scissors}\n")
        print("thats a draw")