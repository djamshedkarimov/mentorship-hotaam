import random

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("welcome to the pypassword generator")
letters = int(input("how many letters should be in ur password?\n"))
symbols = int(input("how many symbols should be in ur password?\n"))
numbers = int(input("how many numbers should be in ur password?\n"))

password_list = []
for char in range(1, letters + 1):
    password_list.append(random.choice(letters_list))

for char in range(1, numbers + 1):
    password_list.append(random.choice(numbers_list))

for char in range(1, symbols + 1):
    password_list.append(random.choice(symbols_list))

random.shuffle(password_list)
for item in password_list:
    print(item, end="")
