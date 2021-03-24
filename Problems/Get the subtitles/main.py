import requests

from bs4 import BeautifulSoup

art_index = input()
art_link = input()

html_response = requests.get(art_link)
article = soup.find
