import requests
from bs4 import BeautifulSoup
from supps.models import Product
from ..extensions import db


def scrape_a1_whey():
    url = 'https://www.a1supplements.com/protein-powder/whey-protein-powder'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    gen = soup.find_all('li', {'class': 'item'})
    rows_logged = 0
    for item in gen:
        product = Product()

        # Dealer Name
        website = 'A1 Supplements'
        product.product_dealer = website

        # Gets the product name
        name = item.find_all('h2', {'class': 'product-name'})[0].text.strip()
        product.product_name = name

        manufacturer = item.find_all('h2', {'class': 'product-name'})[0].text.strip().split()[0]
        product.product_manufacturer = manufacturer

        # Get Product Link
        href = item.find_all('a')[0].get('href')
        product.product_url = href

        # Get Product Price
        price = item.find_all('p', {'class': 'special-price'})[0].text.strip()
        product.product_price = price

        # type of protein
        prod_type = "Protein"
        product.product_type = prod_type

        # Product Image
        image = item.find_all('img')[0].get('data-src')
        product.product_image = image

        # product promos
        promo = item.find_all('div', {'class': 'promo-text'})[0].text.strip()
        product.product_description = promo

        # Per Serving
        r = requests.get(href)
        soup = BeautifulSoup(r.content, "lxml")

        try:
            servings = soup.find_all('span', {'class': 'size-name'})[0].text.split()[0]
            if float(servings) > 10 or float(price[1:]) < 12:
                product.product_price_per_serving = 999
            else:
                pps = format(float(price[1:]) / float(servings), '.2f')
                product.product_price_per_serving = pps
        except IndexError:
            product.product_price_per_serving = 999

        rows_logged += 1
        db.session.add(product)
        db.session.commit()

    print('logged {} rows'.format(rows_logged))

