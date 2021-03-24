import requests

usr_url = input()


def get_url(url):
    return requests.get(url)


response = get_url(usr_url)
if response.status_code:
    if "content" in response.json():
        print(response.json()["content"])
    else:
        print("Invalid quote resource!")
else:
    print(response.content)
