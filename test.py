import requests
from bs4 import BeautifulSoup


url = 'https://www.a1supplements.com/protein-powder/whey-protein-powder'

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

gen = soup.find_all('li', {'class': 'item'})

for item in gen:

    # Dealer Name
    website = 'A1 Supplements'

    # Gets the product name
    name = item.find_all('h2', {'class': 'product-name'})[0].text.strip()
    # print(name)

    manufacturer = item.find_all('h2', {'class': 'product-name'})[0].text.strip().split()[0]
    # print(manufacturer)

    # Get Product Link
    href = item.find_all('a')[0].get('href')
    # print(href)

    # Get Product Price
    price = item.find_all('p', {'class': 'special-price'})[0].text.strip()
    # print(price)

    # type of protein
    prod_type = "Pre-Workout"

    # Product Image
    image = item.find_all('img')[0].get('data-src')
    # print(image)

    # product promos
    promo = item.find_all('div', {'class': 'promo-text'})[0].text.strip()
    # print(promo)

    # Per Serving
    r = requests.get(href)
    soup = BeautifulSoup(r.content, "lxml")

    servings = soup.find_all('span', {'class': 'size-name'})[0].text.split()[0]
    print(servings)
    print(price)

    pps = format(float(price[1:]) / float(servings), '.2f')
    print(pps)

