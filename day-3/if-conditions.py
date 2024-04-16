# water_level = 50
# if water_level > 80:
#   print("drain water")
# else:
#   print("continue")

# if condition1:
#   do A
# elif condition2:
#   do B
# elif condition3:
#   do C

print("welcome to the rollercoaster")
height = int(input("what is ur height? (cm)\n"))
bill = 0

if height >= 120:
  print("ez dub go in the ride but WAIT")
  age = int(input("what is your age?\n"))
  if age < 12:
    bill = 5
    print("you have to pay 5 dollarydoos bc you young")
  elif age <= 18:
    bill = 7
    print("les goo ez teen person discount is 7 dollarydoos")
  elif age > 18:
    bill = 12
    print("ez money in my pockets give 12 dollarydoos buckaroo")

  wants_photo = input("want photo buddy? (y or n)")
  if wants_photo == "y":
    bill += 3
    print("alr thats an extra 3 dollarydoos")
  elif wants_photo == "n":
    print("no extra charge cause someone is in debt")
  else:
    print("what are you on")

  print(f"\nok final bill is {bill}\n")
else:
  print("get taller buddy")

# nested if
# if condition:
#   if another condition:
#     do this
#   else:
#     do this
# else:
#   do this

#logical operators
# A and B -- both have to be True
# C or D -- one of them has to be True
# not E -- reverses a condition. if false, becomes true. if true, becomes false
