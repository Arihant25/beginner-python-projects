import requests
from bs4 import BeautifulSoup

# Get the website content
response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
yc_website = response.text

soup = BeautifulSoup(markup=yc_website, features="html.parser")
# Get all the anchor tags inside tags with class "title"
articles = soup.select('.title > a')
article_texts = [tag.getText() for tag in articles]
article_links = [tag.get("href") for tag in articles]
# Get all the tags containing the points, then remove the word "points" and just keep the number
article_upvotes = [int(tag.getText().split()[0]) for tag in soup.findAll('span', class_="score")]

# Find the article with the highest upvotes and its position in the list
max_upvotes = max(article_upvotes)
index = article_upvotes.index(max_upvotes)

print("The most popular article right now is:")
print(article_texts[index])
print(article_links[index])
