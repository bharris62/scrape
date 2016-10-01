import requests
from bs4 import BeautifulSoup

url = 'http://www.bodybuilding.com/store/whey.html'
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all('a')

gen = soup.find_all('article', {'class': 'product-layout'})

num = 1
for item in gen:
    print(num)
    print(item.find_all('div', {'class': 'product-details'})[0].text)
    num += 1
