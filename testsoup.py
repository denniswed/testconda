# This script is used to test the BeautifulSoup library
# It will create a simple HTML file and parse it using BeautifulSoup
# It will then print the title of the page and the text of the first paragraph
# It will also print the text of all the links in the page
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
print(soup.title)

for link in soup.find_all('a'):
    print(link.get('href'))

tags = soup('img')
for tag in tags:
    print(tag.get('src', None))

print(pd.read_html(str(soup.find("table", {"class": "wikitable"})))[0])

