from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

# year = input("To which year do you want to travel to? Type the date in this format (YYYY-MM-DD): ")

response = requests.get(URL)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
print(soup.prettify())
