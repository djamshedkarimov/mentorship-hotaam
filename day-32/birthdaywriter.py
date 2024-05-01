from datetime import datetime
import pandas
import random
import smtplib
'''importing the recent libraries we have used in the past week'''

MY_EMAIL = "hotaamkarimov07@gmail.com"
MY_PASSWORD = "hotaamkarimov7499839"
'''my email and password'''

today = datetime.now()
today_tuple = (today.month, today.day)
'''a tuple of what day it is'''

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
'''dictionary for birthday!!!'''
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    '''gets random letter txt since there are 3 so your emails dont look as dry as a desert'''
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        '''replaces name to birthday name!!!'''

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
        '''sends email like always by logging into account'''
