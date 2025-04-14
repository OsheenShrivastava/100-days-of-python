import datetime as dt
import random
from smtplib import SMTP
from email.message import EmailMessage

my_email = "pythontestmail123456789@gmail.com"
password = "bazfewpgskkpfpgc"

# TODO-1 - Obtain current day of the week using datatime module
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    # TODO-2 - Open quotes.txt file and obtain a list of quotes
    # Note: The file contains characters that are not valid fo Windows default encoding.
    # UTF-8 encoding is used, which can handle a much wider range of characters than the default Windows encoding.
    with open("quotes.txt", encoding="utf-8") as file:
        all_quotes = file.readlines()

        # TODO-3 - Use random module to pick a random quotes from the list of quotes
        random_quote = random.choice(all_quotes)

    print(random_quote)

    # TODO-4 - Import email.message from EmailMessage module set the details.
    # NOTE: We are using email.message since direct use of f string for this text gives error of ascii codes not
    #  detected.
    msg = EmailMessage()
    msg.set_content(random_quote)
    msg['Subject'] = "Monday Motivation"
    msg['From'] = my_email
    msg['To'] = my_email

    # TODO-5 - Use smtplib to send email to yourself
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(msg)







