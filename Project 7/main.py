import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# -------- Accessed source webpage -------
response = requests.get(url=URL)
response.raise_for_status()

empires_html = response.text
# print(empires_html)

# --------- beautiful soup object creation ------------
soup = BeautifulSoup(empires_html, "html.parser")

# ----------- Accessed relevant sections ------------
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
# --------- Revered the list to ascending format ------------
titles = titles[::-1]
# --------- Split movies names and titles -----------
split = [item.split(")") for item in titles]
# ----------- Index access issue replaced -----------
inner_slice_section = split[11][0].split(":")
split[11] = inner_slice_section
# ----------- Movie numbers accessed -------------
movies_nums = [split[i][0] for i in range(len(split))]
# ----------- Movie titles accessed -------------
movies_names = [split[i][1] for i in range(len(split))]
# ----------- Added final Movies names to 'Movies.txt' files -------------
with open(file="Movies.txt", mode="w") as file:
    file.write(
        "The Top 100 Movies That You Must Watch At-least Once In Your Life.\n"
        "------------------------------------------------------------------\n")
    for i in range(len(movies_nums)):
        file.write(f"{movies_nums[i]}🎥:{movies_names[i]}\n")
print("Writing success")
