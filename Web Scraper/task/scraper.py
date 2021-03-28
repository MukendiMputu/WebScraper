import requests

from bs4 import BeautifulSoup

usr_url = input()
source_file = open('source.html', 'wb')


def get_url(url):
    return requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})


def get_soup(http_response):
    return BeautifulSoup(http_response.content, 'html.parser')


def get_data_byte(http_res):
    return http_res.content


response = get_url(usr_url)
if response.status_code in range(200, 400):
    soup = get_soup(response)
    page_content = get_data_byte(response)
    if source_file.write(page_content):
        print("Content saved.")
    else:
        print("Error writing byte to file")
else:
    print(f"The URL returned {response.status_code}!")
source_file.close()
