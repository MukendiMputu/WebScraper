import requests

from bs4 import BeautifulSoup

usr_url = input()


def get_url(url):
    return requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})


def get_soup(http_response):
    return BeautifulSoup(http_response.content, 'html.parser')


response = get_url(usr_url)
if response.status_code:
    soup = get_soup(response)
    movie_title = soup.find('title')
    description = soup.find('div', {'class': 'summary_text'})
    if not (movie_title and description):
        print("Invalid movie page!")
    else:
        result = {"title": movie_title.text, "description": description.text.strip()}
        print(result)
else:
    print(response.status_code, " - Error")
