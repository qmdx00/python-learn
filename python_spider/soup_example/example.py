from bs4 import BeautifulSoup
import requests
import json

"""
Beautiful Soup 4 example
"""

url = "https://www.140hg.com/"

res = requests.get(url)
html = res.content.decode("utf-8")

soup = BeautifulSoup(html, features="html.parser")
items = soup.find_all(name='div', attrs={'class', "item"})

# save img tags to dict
res = {}
for item in items:  # type: BeautifulSoup
    img = item.find('img')  # type: BeautifulSoup
    res[img.attrs['alt']] = img.attrs['data-original']

json.dump(res, open("movies.json", "w"))
