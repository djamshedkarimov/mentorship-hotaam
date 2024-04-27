#new_list = [new_item for item in list if test]
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}
'''just using for a template in case i use the list comprehension'''

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)
'''adds 1 to each number in numbers
    output: [2, 3, 4'''

numbers = [1, 2, 3]
'''list of numbers'''
new_numbers = [n + 1 for n in numbers]
'''adds 1 to each number in numbers list and appends to new list'''
name = "Hotaam"
'''my name!!!'''
letters_list = [letter for letter in name]
'''finds how much letters are in my name'''
range_list = [num * 2 for num in range(1, 5)]
'''multiplies the number by 2 in the range of 1, 4 (since 5 isnt counted)'''
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
long_names = [name.upper() for name in names if len(name) >= 5]
'''separates short names and long names using list comprehension from the names list
    short_names: add name for every name in names list if the length of the name is less than 5
    long_names: uppercase and add name for every name in names list if the length of the name is more than 4'''

import random

names_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names_list}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

print(students_scores)
print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    print(row)


