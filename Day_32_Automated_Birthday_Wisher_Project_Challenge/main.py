import pandas
import datetime as dt
import random
from smtplib import SMTP

# NOTE: Turn ON 2 step verification,Create app password and edit the password here
my_email = "pythontestmail123456789@gmail.com"
password = "bazfewpgskkpfpgc"

# TODO-1 - Update the birthdays.csv with your friends & family's details

# TODO-2 - Check if today matches a birthday in the birthdays.csv. Create a tuple from today's month and day using
#  datetime
# HINT 1: Only the month and day matter.
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# TODO-3 - Read .csv_file and create a dataframe.
# HINT: Make sure one of the entries matches today's date for testing purposes.
data_frame = pandas.read_csv("birthdays.csv")

# TODO-4 - You could create a dictionary from birthdays.csv that looks like this:
# birthays_dict = {
#     (month, day): data_row
# }

birthday_dict = {(row.month, row.day): row for (index, row) in data_frame.iterrows()}

# TODO-5 - Then you could compare and see if today's month/day matches one of the keys in birthday_dict
if today_tuple in birthday_dict:
    # TODO-6 - Find the birthday person from birthday dictionary
    birthday_person = birthday_dict[today_tuple]
    print(birthday_person)

    # TODO-7 - Create a file path with random letter from letter templates
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    # TODO-8 - Open the file and replace the [NAME] with the person's actual name from birthdays.csv
    with open(file_path) as file:
        data = file.read()
        data = data.replace("[NAME]", birthday_person["name"])

    # TODO-9 - Send the letter generated to that person's email address.
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday\n\n{data}"
        )