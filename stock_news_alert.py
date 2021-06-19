import os
from datetime import date, timedelta
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv('.env')  # Get environment variables

# Get the dates
today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

# Format date as YYYY-MM-DD
yesterday = yesterday.strftime("%Y-%m-%d")
day_before_yesterday = day_before_yesterday.strftime("%Y-%m-%d")

# Change these to the company you're interested in
STOCK = "GOOGL"
COMPANY_NAME = "Google"

# Use AlphaVantage to get stock data
API_KEY = os.getenv('AlphaVantage')
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}

response = requests.get('https://www.alphavantage.co/query', params=parameters)
data = response.json()

# Yesterday
close_0 = float(data['Time Series (Daily)'][yesterday]['4. close'])
# Day before yesterday
close_1 = float(data['Time Series (Daily)'][day_before_yesterday]['4. close'])

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then get the news.
difference = close_1 - close_0
percentage = round(difference/close_0 * 100, 1)

if percentage >= 5 or percentage <= -5:
    # Use NewsAPI to get the first 3 news pieces for the COMPANY_NAME.
    API_KEY = os.getenv("NewsAPI")
    parameters = {
        "qInTitle": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "popularity",
        "apiKey": API_KEY,
        "pageSize": "3",
        "language": "en"
    }

    response = requests.get('https://newsapi.org/v2/everything', params=parameters)
    data = response.json()
    news_list = data['articles']

    news = ""
    for article in news_list:
        news += f"\nHeadline: {article['title']}\n" \
               f"Brief: {article['description']}\n"

    # Use Twilio to send a message with the percentage change and the company news
    account_sid = os.environ.get('account_sid')
    auth_token = os.environ.get('auth_token')
    mobile_number = os.environ.get('mobile_number')

    symbol = "🔺"
    if percentage <= -5:
        symbol = "🔻"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body=f"{STOCK}: {symbol}{abs(percentage)}%\n{news}",
            from_='+15182865347',
            to=mobile_number
        )
