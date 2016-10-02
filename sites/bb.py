import requests
from bs4 import BeautifulSoup

url = 'http://www.bodybuilding.com/store/protein-powder.html'
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

links = soup.find_all('a')

gen = soup.find_all('article', {'class': 'product-layout'})

for item in gen:
    # Gets the product name
    print(item.find_all('div', {'class': 'product-details'})[0].find_all('a')[0].text)

    # TODO Get Product Link

    # Get Product Price
    print(item.find_all('li', {'itemprop': 'price'})[0].text)
    break
