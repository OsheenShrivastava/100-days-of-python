
# TODO-1 - Create a copy of the My Workouts Spreadsheet (attached). You may need to login/register.

# TODO-2 - Go to this link - https://www.nutritionix.com/business/api and select "Get Your API Key" to sign up for a
#  free account. Double check your spam folder (and/or your gmail "promotions" tab) for the Nutritionix verification
#  email.

# TODO-3 - Go to this link - https://developer.nutritionix.com/ . Once logged in, you should be able to access your
#  API key and App id.

# TODO-4 - Import requests module
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# TODO-5 - Create .env file and store all Imp variables in it. Import os and loadenv. Load all the variables from that
#  file. Save your API ID and API KEY after logging to .env file

# Access the environment variables
Api_Id = os.environ["API_ID"]
Api_Key = os.environ["API_KEY"]

# TODO-6 - Obtain URL and create headers. Post request to the url by passing on exercise_params
#  Use the link for:
#  Headers = https://docx.syndigo.com/developers/docs/understand-request-headers
#  API Endpoint for Exercise = https://docx.syndigo.com/developers/docs/natural-language-for-exercise
#  Exercise Parameters = https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise

GENDER = "Female"
WEIGHT_KG = 57
HEIGHT_CM = 5.4
AGE = 29

Exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

Exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": Api_Id,
    "x-app-key": Api_Key,
}

Exercise_params = {
    "query": Exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=Exercise_url, json=Exercise_params, headers=headers)
result = response.json()
print(result)

# TODO-7 - Log into Shetty with this link - https://sheety.co/ with your Google Account (the same account that owns
#  the Google Sheet you copied in step 1).
#  Note 1: Make sure you give Sheety permission to access your Google sheets. If you miss this step, log out of Sheety
#  and log in again.
#  Note 2: Make sure the email matches between your Google Sheet and Sheety Account.

# TODO-8 - Under your Google Account Security settings, you should see that Sheety has access. Double-check that you
#  see Sheety listed as an authorized app. Otherwise, your Python code can't access your spreadsheet.

# TODO-9 - Sign into the Dashboard and Select “New Project” and choose “From Google Sheet”. Paste the URL of the
#  spreadsheet into the box and Check the sheet names look correct. Finally, Click “Create Project”.

# TODO-10 - Click on the workouts API endpoint and enable GET and POST.

# TODO-11 - Write some code to use the Sheety API to generate a new row of data in your Google Sheet for each of the
#  exercises that you get back from the Nutritionix API. The date and time columns should contain the current date and
#  time from the Python datetime module.
#  Obtain Sheety endpoint from .env file.

today = datetime.now()
Date = today.strftime("%Y/%m/%d")
Time = today.strftime("%H:%M:%S")
# print(Date, Time)

# TODO-12 - Add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it.
#  We are moving forward with Basic Authentication involving a username and password
#  Copy Username,Password and save them to .env file.

# Access the environment variables
Sheet_endpoint = os.environ["SHEETY_ENDPOINT"]
Username = os.environ["AUTH_USERNAME"]
Password = os.environ["AUTH_PASSWORD"]

for exercise in result["exercises"]:
    Workout_params = {
        "workout": {
            "date": Date,
            "time": Time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # TODO-13 - Post a request to authenticate using basic authentication
    workout_response = requests.post(url=Sheet_endpoint, json=Workout_params, auth=(Username, Password))
    workout_result = workout_response.json()
    print(workout_result)