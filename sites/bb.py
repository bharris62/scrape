import requests
from bs4 import BeautifulSoup

url = 'http://www.bodybuilding.com/store/whey.html'
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all('a')

gen = soup.find_all('article', {'class': 'store-layout-product-item'})

for item in gen:
    print(item.contents[1].find_all('a')[2])