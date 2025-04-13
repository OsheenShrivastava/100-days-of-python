import requests
from datetime import datetime
from smtplib import SMTP
import time

# TODO-1 - Edit your Latitude,Longitude,email and password
# Try: To test the code you can change MY_LAT and MY_LONG to curent ISS co-ordinates
MY_LAT = "Your latitude"
MY_LONG = "Your longitude"

# NOTE: Turn ON 2 step verification,Create app password and edit the password here
my_email = "Your email_id"
password = "Your Password"


# TODO-10 - Create is_iss_overhead() function and return true if iss is close to my current position
def is_iss_overhead():
    # TODO-2 - Request response from iss api,raise exceptions and parse data to json
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # TODO-3 - Separate iss_lat and iss_long data and save them
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude, iss_longitude)


    # TODO-4 - Check if your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


# TODO-11 - Create is_night() function and return true if it is currently dark
def is_night():
    # TODO-5 - Create a dictionary of parameters and store your lat,long and formatted
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # TODO-6 - Request response from sunrise and sunset api,raise exceptions and parse data to json
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # TODO-7 - Separate sunrise and sunset data and save them
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # TODO-8 - Import datetime module and find out current hour
    time_now = datetime.now().hour

    # TODO-9 - Check if its currently dark, if yes then return true
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    # TODO-14 - Run the code every 60 seconds
    time.sleep(60)
    print("60 secs over")
    # TODO-12 - Check if is_iss_overhead and is_night are both true. If yes then send email
    if is_iss_overhead and is_night():
        print("sending")
        # TODO-13 - Open connection,add login details and send mail
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject: Look up \n\n The ISS is above you in the sky"
            )


