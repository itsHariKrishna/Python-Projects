from bs4 import BeautifulSoup
import requests


year = input("To which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{year}"


response = requests.get(URL)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

# titles = soup.select(selector="div li h3.a-no-trucate")
titles = soup.select(selector="div li h3.a-no-trucate")
song_titles = [i.getText().strip("\n\t") for i in titles]
print(song_titles)
# song_titles = [title_name.text for title_name in titles]
# print(song_titles)
