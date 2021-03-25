import requests

from bs4 import BeautifulSoup

query_word = input()
link_to_story = input()

r = requests.get(link_to_story)
soup = BeautifulSoup(r.content, 'html.parser')

paragraphs = soup.find_all('p')

for paragraph in paragraphs:
    if query_word in paragraph.text:
        print(paragraph.text)
        break
