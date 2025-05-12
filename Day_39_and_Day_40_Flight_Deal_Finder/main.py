# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
import os
from dotenv import load_dotenv
import time
from datetime import datetime, timedelta
from flight_data import FlightData
from notification_manager import NotificationManager

# TODO-1 - Import requests module in data_manager.py file and save the google sheet endpoint in a variable

# TODO-2 - Create a class called DataManager and Use request module to GET data from google sheet

# TODO-3 - Import pprint so that formatted data can be printed

# TODO-4 - Pass everything stored in the "prices" key back to the main.py file and store it in a variable called
#  sheet_data, so that you can print the sheet_data from main.py

# TODO-5 - Pass each city name in sheet_data one-by-one to the FlightSearch class. For now, the FlightSearch class can
#  respond with "TESTING" instead of a real IATA code. You should use the response from the FlightSearch class to update
#  the sheet_data dictionary

# TODO-6 - In the DataManager Class make a PUT request and use the row id from sheet_data to update the Google Sheet
#  with the IATA codes. If successful, you should see the Google Sheet update as if by magic

# TODO-7 - Enable Basic Authentication for your sheety project. Create a .env file that will hold all your secrets like
#  your username, password, and token information. Import os and loadenv. Load all the variables from that file.
#  Save your Username and Password after logging to .env file

# TODO-8 - Pass Username and Password in datamanager.put_request() function.

# TODO-9 - Delete the "TESTING" values in the Google sheet again. Our code thus far only writes to the Google sheet if
#  the cells are empty. You'll have to sign up (free) for an account with Amadeus to access their flight search API.

# TODO-10 - For this project, let's do the Amadeus authentication inside our flight_search.py file.
#  Create an __init__(self)  in the FlightSearch class. Then give FlightSearch three variables: an _api_key,
#  an _api_secret, and a _token. set your token by calling a separate method where you'll request the token.

# TODO-11 - To make any requests to Amadeus, you first need a token (the Amadeus API key and Secret is not sufficient).
#  Create a function called _get_new_token(self) where you request a new token using your API keys.

# TODO-12 - Once,response form AMADEUS_IATA_ENDPOINT datapoint is received then segregate the data such that only city
#  code is obtained. Then replace the "iataCode" code of sheet in the same FOR loop with the city code. Add exception
#  handling.

# TODO-13 - Once the city code is obtained then write it to google sheet using data_manager.py

# TODO-14 - The next step is to search for the flight prices from London (LON) to all the destinations in the Google
#  Sheet. In this project, we're looking only for non stop flights, that leave anytime between tomorrow and in 6 months
#  (6x30days) time. We're also looking for round trips for 1 adult. The currency of the price we get back should be in
#  GBP.

# TODO-15 - Create a function called check_flights in flight_search.py and get the json response from its endpoint.
#  Print the response status code if response is not equal to 200.

# TODO-16 - Import date time module in main.py and use timedelta function to find date of tomorrow and six months after
#  tomorrow.

# TODO-17 - Create a FOR loop in main.py to run through all data in google sheet.

# TODO-18 - Use the FlightData class to represent the flight data. e.g. You can create attributes for price,
#  departure_airport_code etc. Create a function called find_cheapest_flight() that parses the JSON data returned from
#  your FlightSearch. Add some error handling e.g., if that data is None.

# TODO-19 - Finally return the cheapest price for all flights from LON to every city in the sheet

# TODO-20 - Check if any of the flights found are cheaper than the Lowest Price listed in the Google Sheet. If so, then
#  you should use the Twilio API to send an SMS with enough information to book the flight. Add Twilio ID, Auth Token,
#  Virtual number, and Verified number to your .env file. Import Notification Manager class from notification_manager.py
#  for this job. Use error handling method in case of error if received data is N/A.

# TODO-21 - Initialize the NotificationManager class in main.py and pass the Twilio parameters:
#  Twilio_Account_Sid, Twilio_Auth_Token, Twilio_SMS_Number, Twilio_Whatsapp_Number and Twilio_Verified_Number

# TODO-22 - Create two methods, 1 for sending normal SMS and another for Whatsapp message functions inside
#  notification_manager.py file

# TODO-23 - Call either one of the methods of sending notification to verified number in FOR loop of main.py

# TODO-24 - If a direct flight is not found, search Amadeus one more time for that destination to see if there are
#  indirect flights (flights with 1 stop or 2 stops) instead. Capture the cheapest flight price for a flight with a
#  stopover. In the flight_data.py, add a variable called stops to your __init__() method to capture how many stops a
#  flight has and also to the return statement.

# TODO-25 - A flight with 2 segments will have 1 stop, so if we calculate number of stops(nr_stops) it will be equal to
#  (length of segments - 1). Add nr_stops in finding final destination as Final destination is found in the last segment
#  of the flight. Return nr_stops from find_cheapest_flight function.

# TODO-26 - If there are no direct flights i.e., N/A is returned for any of the flight then search for Indirect flight

# TODO-27 - Pass a parameter called is_direct in flightsearch.check_flights() function. It is set to True in order to
#  run loop for Direct flights and then it is passed as False to run loop for Indirect flights.

# TODO-28 - Save users and prices google sheet endpoints in .env file. Pass prices endpoint in DataManager class and
#  datamanager.put_request() method. Pass users endpoint in datamanager.get_customer_emails() method.

# TODO-29 - Import pprint in data_manager.py file. Receive the response from users sheet endpoint and return it in
#  main.py

# TODO-30 - Convert the data to a list using list comprehension

# TODO-31 - Update your .env file with your SMTP address, your email, and your app password.

# TODO-32 - Pass SMTP address, your email, and your app password in NotificationManager class and initialize them as
#  self variables

# TODO-33 - Create a method in the NotificationManager class called send_emails()

# TODO-34 - when sending emails, it won't like the "£" symbol, you will get value error and the email won't be sent.
#  So add .encode('utf-8') at the end of message to encode it to utf 8.

# Load the .env file
load_dotenv()

# Access the environment variables
Username = os.environ["AUTH_USERNAME"]
Password = os.environ["AUTH_PASSWORD"]
Api_Key = os.environ["API_KEY"]
Api_Secret = os.environ["API_SECRET"]
Twilio_Account_Sid = os.environ["TWILIO_ACCOUNT_SID"]
Twilio_Auth_Token = os.environ["TWILIO_AUTH_TOKEN"]
Twilio_SMS_Number = os.environ["VIRTUAL_SMS_NUMBER"]
Twilio_Whatsapp_Number = os.environ["VIRTUAL_WHATSAPP_NUMBER"]
Twilio_Verified_Number = os.environ["VERIFIED_NUMBER"]
Flight_Deals_Sheet_Price_Endpoint = os.environ["FLIGHT_DEALS_SHEET_PRICE_ENDPOINT"]
Users_Data_Sheet_Endpoint = os.environ["USERS_DATA_SHEET_ENDPOINT"]
SMTP_Address = os.environ["SMTP_ADDRESS"]
Email = os.environ["EMAIL"]
App_Password = os.environ["APP_PASSWORD"]

ORIGIN_CITY = "LON"
stops = 0
stopover_flights = None

notification_manager = NotificationManager(Twilio_Account_Sid, Twilio_Auth_Token, Twilio_SMS_Number,
                                           Twilio_Whatsapp_Number, Twilio_Verified_Number, SMTP_Address, Email,
                                           App_Password)

datamanager = DataManager(Username, Password, Flight_Deals_Sheet_Price_Endpoint)
pprint(datamanager.data)
sheet_data = datamanager.data["prices"]

# Note: Since we have use a list, so we are passing sheet_data[0] and then ["iataCode"]

flightsearch = FlightSearch(Api_Key, Api_Secret)

if sheet_data[0]["iataCode"] == "":
    flightsearch.Add_data_to_iataCode_row(sheet_data)
    time.sleep(2)

pprint(f"sheet_data:\n {sheet_data}")

datamanager.put_request(sheet_data, Username, Password, Flight_Deals_Sheet_Price_Endpoint)
# pprint(sheet_data)

# Date time
today = datetime.today()
tomorrow = today + timedelta(days=1)
Date_6_months_from_tomorrow = tomorrow + timedelta(days=6 * 30)
# print(tomorrow.date())
# print(Date_6_months_from_tomorrow.date())


customer_data = datamanager.get_customer_emails(Username, Password, Users_Data_Sheet_Endpoint)

customer_email_list = [data["whatIsYourEmail"] for data in customer_data]
print(f"Your email list includes {customer_email_list}")


# ============================ Search for direct flights ============================

for destination in sheet_data:

    flights = flightsearch.check_flights(
        ORIGIN_CITY,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=Date_6_months_from_tomorrow,
    )
    # pprint(flights)

    flightdata = FlightData(flights, ORIGIN_CITY, destination["iataCode"], tomorrow, Date_6_months_from_tomorrow, stops)
    cheapest_flight = flightdata.find_cheapest_flight(flights)

    print(f"{destination['city']}: £{cheapest_flight.price}")

    time.sleep(2)

    # ============================ Search for indirect flight if N/A ============================
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")

        stopover_flights = flightsearch.check_flights(
            ORIGIN_CITY,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=Date_6_months_from_tomorrow,
            is_direct=False,
        )

        flightdata = FlightData(stopover_flights, ORIGIN_CITY, destination["iataCode"], tomorrow,
                                Date_6_months_from_tomorrow, stops)
        cheapest_flight = flightdata.find_cheapest_flight(stopover_flights)

        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")

    # ============================ Send Notifications and Emails ============================
    try:
        if float(cheapest_flight.price) < float(destination['lowestPrice']):
            if cheapest_flight.stops == 0:
                message_body = f"Low price alert! Only £{cheapest_flight.price} to fly from " \
                               f"{cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, on " \
                               f"{cheapest_flight.out_date} until {cheapest_flight.return_date}."
            else:
                message_body = f"Low price alert! Only £{cheapest_flight.price} to fly from " \
                               f"{cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                               f"with {cheapest_flight.stops} stop(s) departing on {cheapest_flight.out_date} and " \
                               f"returning on {cheapest_flight.return_date}."

            # Normal SMS
            notification_manager.send_sms(message_body)

            # Whatsapp SMS
            # notification_manager.send_whatsapp_sms(message_body)

            # Email
            print(f"Check your email. Lower price flight found to {destination['city']}!")
            notification_manager.send_emails(customer_email_list, message_body)
    except ValueError:
        print("Value error")

pprint(sheet_data)