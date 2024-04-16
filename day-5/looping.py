fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits)

print("\n ")
# range()
# for number in range(a, b):
#   print(number)
total = 0
for number in range(1, 101):
    total += number
print(total)
print("\n")

target = 15
for number in range(1, target + 1):
    if number % 5 == 0 and number % 3 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)