import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)

random_float = random.random()
print(random_float)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "California", "Ohio"]
states_of_america[1] = "Pencilvania"
print(states_of_america)
states_of_america.append("skibidi")
print(len(states_of_america))
print(states_of_america)


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)