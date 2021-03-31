import os
import string

import requests
from bs4 import BeautifulSoup

usr_url = "https://www.nature.com/nature/articles"


def get_url(url):
    return requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})


def get_soup(http_response):
    return BeautifulSoup(http_response.content, 'html.parser')


def get_data_byte(http_res):
    return http_res.content


def clean_title(title_list):
    clean_list = [title.replace(" ", "_") for title in title_list]
    return clean_list


numb_of_pages = int(input())
type_of_articles = input()

for page in range(1, numb_of_pages + 1):
    response = get_url(usr_url + '?searchType=journalSearch&sort=PubDate&page=' + str(page))
    dir_name = 'Page_' + str(page)
    os.mkdir(dir_name)
    if response.status_code in range(200, 400):
        soup = get_soup(response)
        article_links = [anchor.attrs['href'] for anchor in
                         soup.find_all('a', {'data-track-action': 'view article'})]
        for link in article_links:
            page_link = "https://www.nature.com"
            page_link += link
            r = get_url(page_link)  # get content in article page
            if r.status_code in range(200, 400):
                s = get_soup(r)
                if s.find('meta', {'name': 'dc.type', 'content': type_of_articles}):
                    replace_punctuation = str.maketrans('', '', string.punctuation)
                    file_name = s.find('h1', {'class': 'article-item__title', 'itemprop': 'headline'}) \
                        .text.strip() \
                        .translate(replace_punctuation) \
                        .replace(' ', '_')
                    file_name = os.path.join(dir_name, file_name)
                    file_content = s.find('div', {'class': 'article-item__body'}) \
                        or s.find('div', {'class': 'article__body'}) \
                        if s.find('div', {'class': 'article-item__body'}) \
                        or s.find('div', {'class': 'article__body'}) else ''
                    if file_content:
                        file_content = file_content.text.strip()
                    source_file = open(f'{file_name}.txt', 'wb')
                    source_file.write(bytes(file_content, 'utf-8'))
                    source_file.close()
    else:
        print(f"The URL returned {response.status_code}!")
print("Saved all articles.")
