# key: value
# bug: moth in your computer

my_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
    "Bug2": {
        "Function2": "A piece of code that you can easily"
    }
}

print(my_dictionary["Bug2"]["Function2"])

print(my_dictionary["Bug"])

my_dictionary["Loop"] = "The action of doing something over and over again."
print(my_dictionary)

my_dictionary = {}
print(my_dictionary)

my_dictionary["Bug"] = "A moth in your computer"
print(my_dictionary["Bug"])

my_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again."
}

for key in my_dictionary:
    print(key)
    print(my_dictionary[key])

print("\n")
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
# list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#dictionary in dictionary

travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# dictionary in a list
travel_yay = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]

print(travel_yay[0]["cities_visited"])
print(travel_yay[1]["cities_visited"])