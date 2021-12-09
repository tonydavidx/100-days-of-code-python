import os
import requests
import math
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

stock_opts = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": 'compact',
    "apikey": os.getenv("ALPHAVANTAGE_API")
}

news_opts = {
    "q": COMPANY_NAME,
    "sortBy": "newest",
    "apiKey": os.getenv("NEWS_API")
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_opts)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
# print(stock_data)
# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
daily_stock_price = []
for date, price in stock_data.items():
    daily_stock_price.append(float(price['4. close']))

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday_stock_price = daily_stock_price[1]
day_before_yesterday_stock_price = daily_stock_price[2]
# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
stock_difference = abs(yesterday_stock_price -
                       day_before_yesterday_stock_price)
difference_percentage = (
    stock_difference / day_before_yesterday_stock_price) * 100

print(difference_percentage)
# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

news_response = requests.get(NEWS_ENDPOINT, params=news_opts)
news_response.raise_for_status()
news_data = news_response.json()['articles']

company_news = news_data[:3]
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.


if difference_percentage > 5:
    for i in range(3):
        message = client.messages.create(
            body=f"{STOCK_NAME} {math.floor(difference_percentage)} \nHeadline: {company_news[i]['title']}\nBrief: {company_news[i]['description']}",
            from_='+18043737869',
            to='+919600134756'
        )
else:
    print("No News")

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
