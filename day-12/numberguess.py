import random

#getting all the inputs
print("welcome to very fun awesome number game")
number = random.randint(1, 100)
print("thinking of random number 1-100")
difficulty = input("choose a difficulty (easy or hard): ").lower()
attempts = 0

if difficulty == "easy":
    # easy difficulty (for newbies)
    attempts = 10
    while attempts > 0:
        #while you have attempts
        guess = int(input(f"you have {attempts} attempts to find the number: "))
        if guess == number:
            #hooray winner winner chicken dinner
            print("yay!!! you guessed the number.")
            break
            # breaks out of while loop since you win
        elif guess < number:
            #too low
            print("too low. try again.")
        else:
            # too high
            print("too high. try again.")
        attempts -= 1
        # -1 attempt
    else:
        #used up all of attempts
        print("sorry, you've used all your attempts. the number was:", number)
elif difficulty == "hard":
    # hard for pros
    attempts = 5
    while attempts > 0:
        # while attempts greater than 0
        guess = int(input(f"You have {attempts} attempts to find the number: "))
        if guess == number:
            # winner winner chicken dinner
            print("yay!! you guessed the number.")
            break
        elif guess < number:
            # too low
            print("too low. try again.")
        else:
            #too high
            print("too high. try again.")
        attempts -= 1
        #-1 attempt
    else:
        #use up all attempts
        print("sorry, you've used all your attempts. the number was:", number)
else:
    #invalid input
    print("invalid input. please choose either 'easy' or 'hard'.")

