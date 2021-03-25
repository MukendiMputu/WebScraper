import requests

from bs4 import BeautifulSoup

art_index = int(input())
art_link = input()

html_response = requests.get(art_link)
if html_response.status_code:
    html_soup = BeautifulSoup(html_response.content, 'html.parser')
    html_code = html_soup.prettify()
    subtitles = html_soup.find_all('h2')
    print(subtitles[art_index].text)
else:
    print('Page not found!')
