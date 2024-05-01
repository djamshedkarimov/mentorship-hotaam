# import smtplib
'''import smptblib!!!'''
#
# my_email = "hotaamkarimov07@gmail.com"
# password = "hotaamkarimov7499839"
'''my user and password'''
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
'''logs into my account'''
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="testingacc0403@gmail.com",
#         msg="Subject: Hello\n\nThis is the body of my email"
'''sends an email from one account to another using smtplib'''
#     )


# import datetime as dt
'''datetime used for finding time'''
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
'''you can find year, month, day, second, and even milliseconds. it is really specific'''
#
# date_of_birth = dt.datetime(year=2011, month=4, day=3, hour=7, minute=47, second=32)
# print(date_of_birth)
'''my date of birth (last three are fake)'''

import smtplib
import datetime as dt
import random

my_email = "hotaamkarimov07@gmail.com"
my_password = "hotaamkarimov7499839"
'''logging into my account'''

now = dt.datetime.now()
weekday = now.weekday()
'''weekday is what day it is right now in index form
    monday = 0
    tuesday = 1
    it keeps going up'''
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        '''if weekday is tuesday, it grabs a random quote from quote txt'''

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: hi this for cool python\n\n{quote}")
        '''sends quote as an email to myself'''


