from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2"

# Get the list of top 100 movies
article = requests.get(url).text
soup = BeautifulSoup(article, "html.parser")
movies = [movie.getText()
          for movie in soup.findAll(name="h3", class_="title")][::-1]

# Write the list to movies.txt
with open("./top_100_movies/movies.txt", "w") as file:
    file.write("\n".join(movies))
