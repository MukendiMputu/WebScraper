import requests

from bs4 import BeautifulSoup

usr_url = "https://www.nature.com/nature/articles"
# source_file = open('source.html', 'wb')


def get_url(url):
    return requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})


def get_soup(http_response):
    return BeautifulSoup(http_response.content, 'html.parser')


def get_data_byte(http_res):
    return http_res.content


def clean_title(title_list):
    clean_list = [title.replace(" ", "_") for title in title_list]
    return clean_list


response = get_url(usr_url)
if response.status_code in range(200, 400):
    soup = get_soup(response)
    article_titles = [anchor.text for anchor in
                      soup.find_all('a', {'data-track-action': 'view article'})
                      ]
    article_links = [anchor.attrs['href'] for anchor in
                     soup.find_all('a', {'data-track-action': 'view article'})
                     ]
    article_types = [type_text.text.strip() for type_text in
                     soup.find_all('span', {'data-test': 'article.type'})
                     ]
    print(article_titles)
    print(article_types)
    # page_content = get_data_byte(response)
    # if source_file.write(page_content):
    #     print("Content saved.")
    # else:
    #     print("Error writing byte to file")
else:
    print(f"The URL returned {response.status_code}!")
# source_file.close()
