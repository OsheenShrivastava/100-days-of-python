# TODO-1 - Import Requests
import requests
from twilio.rest import Client
import os

from dotenv import load_dotenv

# Load the .env file
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_MARKET_API_KEY = "Your Stock Market API Key"
NEWS_API_KEY = "Your News API Key"

# Access the environment variables
# Note: Smit's twilio account credentials are used inthis code
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# TODO 2. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_MARKET_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

Yesterday_data = data_list[0]
Yesterday_closing = Yesterday_data["4. close"]
print(Yesterday_closing)

# TODO 2. - Get the day before yesterday's closing stock price

Day_before_Yesterday_data = data_list[1]
Day_before_Yesterday_closing = Day_before_Yesterday_data["4. close"]
print(Day_before_Yesterday_closing)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp

"""
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
    file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of
    the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
    file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
    of the coronavirus market crash.
    """
Difference = (float(Yesterday_closing) - float(Day_before_Yesterday_closing))
up_down = None
if Difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.

Percentage_difference = round((Difference / float(Yesterday_closing)) * 100)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(Percentage_difference) > 5:
    print("Get News")

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
    #  Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{Percentage_difference}%\nHeadline: {article['title']}.\nBrief: {article['description']}"for article in three_articles]
    print(formatted_articles)

    # TODO 9. - Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)

    # Optional TODO: Format the message like this:
    for article in formatted_articles:
        # Whatsapp message
        message = client.messages.create(
            body=article,
            from_="whatsapp:Your Twilio Whatsapp Number ",
            to="whatsapp:Your Mobile Number",
        )