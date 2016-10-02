import requests
from bs4 import BeautifulSoup

url = 'http://www.bodybuilding.com/store/protein-powder.html'
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

gen = soup.find_all('article', {'class': 'product-layout'})
print(gen)

for item in gen:
    # Dealer Name
    print('bodybuilding.com')

    # Gets the product name
    print(item.find_all('div', {'class': 'product-details'})[0].find_all('a')[0].text)

    # Get Product Link
    href = item.find_all('h3')[0].find('a').get('href')
    print('https://bodybuilding.com%s' %(href))

    # Get Product Price
    price = item.find_all('li', {'itemprop': 'price'})[0].text
    print(price)

    # Per Serving
    servings = item.find_all('li', {'class': 'product-spec'})[2].text[11:]

    # Price per serving
    print(format(float(price[1:])/int(servings), '.2f'))

    # type of protein
    print("Whey")

    # Product Image
    image = item.find_all('img')[0].get('src')
    print(image)
    break
