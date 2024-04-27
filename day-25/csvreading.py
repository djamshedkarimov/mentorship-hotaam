# with open("weather_data.csv") as data_file:
    # data = data_file.read_lines()
    # print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].mean)
# print(data["temp"].max())
#
#
# print(data["condition"])
# print(data.condition)


# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# temp_monday_F = (monday.temp * 9/5) + 32
# print(temp_monday_F)
#
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# school_data = pandas.DataFrame(data_dict)
# school_data.to_csv("school_data.csv")
#

import pandas
data = pandas.read_csv("squirrel_data.csv")

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

temporary_dict = {
    "Fur Color": ["Grey", "Black", "Cinnamon"],
    "Count": [grey_count, black_count, cinnamon_count]
}
shortened_squirrel_data = pandas.DataFrame(temporary_dict)
shortened_squirrel_data.to_csv("shortened_squirrel_data.csv")

