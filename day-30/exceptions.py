'''File not found'''
# with open("a_file.txt") as file:
#     file.read()

'''Key error'''
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

'''IndexError'''
# fruit_list = ["apple", "banana", "pear"]
# pear = fruit_list[3]

'''TypeError'''
# text = "abc"
# print(text + 5)

'''4 steps for catching exceptions
    1. try: something that might cause an exception
    2. except: do this if there was an exception
    3. else: do this if there were no exceptions
    4. finally: do this no matter what happens
    '''

'''solving exceptions'''
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("skibidi toilet")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("haha i made this error up")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("you entered an unrealistic height")

bmi = weight / height ** 2
print(bmi)