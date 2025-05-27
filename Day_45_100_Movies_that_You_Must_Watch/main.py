
# TODO-1 - Import Requests module and BeautifulSoup from bs4 module

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# TODO-2 - Request data from URL, check its status and store the response in a variable

response = requests.get(url=URL)
response.raise_for_status()
webpage = response.text

# TODO-3 - Initialize Beautiful Soup and parse the data in html

soup = BeautifulSoup(webpage, "html.parser")
Movies_list = soup.find_all(name="h3", class_="title")

# TODO-4 - Run FOR Loop and store the movies into a list in a reversed manner using slicing. Encode them in "latin" so
#  to avoid any errors

list_1 = [movie.text.encode('latin1') for movie in Movies_list[::-1]]

# TODO-5 - Open movies.txt file. Run a FOR loop for list_1, decode the movie list using utf-8 and write them to
#  .txt file

with open("movies.txt", mode="w") as file:
    for movie in list_1:
        clean_movie = movie.decode("utf-8")
        file.write(clean_movie + "\n")