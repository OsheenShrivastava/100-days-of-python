
#  Try: Go to API Call and copy the string. Edit it by entering your location latitude,longitude and api key to check
#  weather data
#  https://api.openweathermap.org/data/2.5/weather?lat=your_lat&lon=your_long&appid=your_api_key

# TODO-1 - Import requests module
import requests

# TODO-7 - Import Client from twilio and os
import os
from twilio.rest import Client

# TODO-8 - Copy and paste your own account_sid and auth_token from your account to .env.py file

# TODO-9 - Import dotenv and load .env (environment) files
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# TODO-2 - Create your account on https://openweather.co.uk/ , go here -> https://home.openweathermap.org/api_keys
#  and copy your api key
api_key = "Your api key"

MY_LAT = "Your Latitude"
MY_LONG = "Your Longitude"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# TODO-10 - Make sure the assignment of account_sid and auth_token is done as shown below
# NOTE: Edit your variables in .env file
# Access the environment variables
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


# TODO-3 - Create a json string for parameters to be passed
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

# TODO-4 - Request data from url, raise exceptions, convert and store the data in json
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

# TODO-6 - Create a FOR loop to check throughout the data if id_data < 700. If true then print "Bring an Umbrella"
will_rain = False

for id_no in data["list"]:
    # TODO-5 - Find weather id from the data and store it in a variable
    id_data = id_no["weather"][0]["id"]
    if int(id_data) < 700:
        will_rain = True

if will_rain:
    # TODO-11 - Initialize the Client
    client = Client(account_sid, auth_token)

    # NOTE: Sign up with Twilio and obtain your free Twilio Number

    # Method 1 - SMS
    # TODO-12 - Form the body of message and print message status
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="Your Twilio free Number",
        to="Your Mobile Number",
    )

    # Method 2 - Whatsapp message
    # message = client.messages.create(
    #     body="It's going to rain today. Remember to bring an ☔",
    #     from_="whatsapp:'Your Whatsapp Twilio free Number'",
    #     to="whatsapp:'Your Mobile Number'",
    # )

    print(message.status)