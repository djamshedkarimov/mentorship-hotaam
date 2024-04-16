from game_data import data
import random

print("welcome to the super awesome ultra omega higher lower game!")
print("instructions: there will be 2 random celebrities and you have to find which one has a higher following count!!")
print("if you guess correctly, we use the correct answer and generate another random celebrity to repeat!")
print("if you lose.. thats on you\n")

account1 = random.choice(data)
account2 = random.choice(data)
following1 = account1['follower_count']
following2 = account2['follower_count']
score = 0
if account1 == account2:
    account2 = random.choice(data)

def get_input():
    account1 = random.choice(data)
    account2 = random.choice(data)
    print(f"{account1['name']}, {account1['description']} in {account1['country']}\nvs\n{account2['name']}, {account2['description']} in {account2['country']}")
    guess = int(input(f"input '1' for {account1['name']} or input '2' for {account2['name']}\n"))
    following1 = account1['follower_count']
    following2 = account2['follower_count']
    check(guess, following1, following2)

def check(guess, following1, following2):
    global score
    global account1
    global account2
    if guess == 1:
        if following1 > following2:
            print("you got it right!")
            score += 1
            print(f"your score is {score}\n")
        elif following1 == following2:
            print("it was the same... but we count it!")
            score += 1
            print(f"your score is {score}\n")
        else:
            print("you got it wrong\n")
            print(f"your score is {score}\n")
    elif guess == 2:
        if following2 > following1:
            print("you got it right!")
            score += 1
            print(f"your score is {score}\n")
        elif following1 == following2:
            print("it was the same... but we count it!")
            score += 1
            print(f"your score is {score}v")
        else:
            print("you got it wrong")
            print(f"your score is {score}\n")
    get_input()

print(f"{account1['name']}, {account1['description']} in {account1['country']}\nvs\n{account2['name']}, {account2['description']} in {account2['country']}")
guess = int(input(f"input '1' for {account1['name']} or input '2' for {account2['name']}\n"))
check(guess, following1, following2)