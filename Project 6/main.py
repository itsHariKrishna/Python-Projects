from bs4 import BeautifulSoup
import requests

# Access of ycombinator website (hacker news)
response = requests.get(url="https://news.ycombinator.com/news")
response.raise_for_status()

# Parsing HTML from the site response
parsed_html = response.text
soup = BeautifulSoup(parsed_html, "html.parser")

# Accessing required part of website.
article_details = soup.find_all("a", class_="titlelink")  # find all anchor tags for specific class
article_titles = [tag.getText() for tag in soup.find_all("a", class_="titlelink")]  # get the title
article_links = [link.get(key="href") for link in article_details]  # get article links
article_upvotes = [int(upvote.getText().split()[0]) for upvote in
                   soup.find_all("span", class_="score")]  # get article upvote

# get highest article upvote
highest_vote = max(article_upvotes)
highest_index = article_upvotes.index(highest_vote)

# final output
hot_news = {
    'Highest Up-Vote': highest_vote,
    'Title': article_titles[highest_index],
    'Link': article_links[highest_index],
}
print(hot_news)
