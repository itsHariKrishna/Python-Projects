import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Twilio detail
account_sid = "user account sid"
auth_token = "user auth tocken"

NEWS_API_KEY = "d2e1b0e707594978b1fb40bb40653aab"
STOCK_API_KEY = "R73XAV49MORTQTDW"  # Stock API key

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}
stock_resp = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_resp.raise_for_status()

user_date_yesterday = input("Enter the yesterday's date 'yyyy-mm-dd': ")
user_date_before_yesterday = input("Enter the day before yesterday's date 'yyyy-mm-dd': ")

stock_data_yesterday = float(stock_resp.json()['Time Series (Daily)'][user_date_yesterday]['4. close'])
stock_data_day_before_yesterday = float(
    stock_resp.json()['Time Series (Daily)'][user_date_before_yesterday]['4. close'])


# stock_data_yesterday = float(stock_resp.json()['Time Series (Daily)']['2022-04-08']['4. close'])
# stock_data_day_before_yesterday = float(stock_resp.json()['Time Series (Daily)']['2022-04-07']['4. close'])


def percent_calc(yesterday_price, day_before_yesterday_price):
    # % diff calculation formula: [|A - B| / [(A + B) / 2]] * 100
    return int(((abs(stock_data_day_before_yesterday - stock_data_yesterday)) / (
            (stock_data_day_before_yesterday + stock_data_yesterday) / 2)) * 100)


price_diff = percent_calc(stock_data_yesterday, stock_data_day_before_yesterday)
if price_diff < -2 or price_diff > 2:

    news_params = {
        'q': COMPANY_NAME,
        'apiKey': NEWS_API_KEY,
    }

    news_resp = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_resp.raise_for_status()

    news_data_description = [news_resp.json()['articles'][:4][description]['description'] for description in range(4)]
    news_data_titles = [news_resp.json()['articles'][:4][title]['title'] for title in range(4)]


    def send_msg():
        client = Client(account_sid, auth_token)
        for i in range(4):
            message = client.messages \
                .create(
                body=f"TSLA: 🔺{price_diff}%\nHeadline: {news_data_titles[i]}\nBrief: {news_data_description[i]}",
                from_='PHONE NUMBER',
                to='PHONE NUMBER'
            )


    send_msg()
