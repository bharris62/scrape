import requests
from bs4 import BeautifulSoup
import re

from supps.models import Product
from supps.extensions import db


def scrape_vitamin_shoppe_vitamin():
    url = 'http://www.vitaminshoppe.com/c/men-s-multivitamins/N-893'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    rows_logged = 0

    gen = soup.find_all('div', {'class': 'listing'})

    for item in gen:

        product = Product()

        # Dealer Name
        website = 'Vitamin Shoppe'
        product.product_dealer = website

        # Get the product name
        product_name = item.find_all('span', {'itemprop': 'name'})[0].text
        product.product_name = product_name

        # Get product manufacturer
        prod_manufacturer = item.find_all('span', {'itemprop': 'brand'})[0].text
        product.product_manufacturer = prod_manufacturer.split()[0]

        # Get Product Link
        url_ext = item.find_all('a', {'class': 'gray-link'})[0].get('href')
        link = 'https://www.vitaminshoppe.com%s' % url_ext
        product.product_url = link

        # Get Product Price
        dollar = item.find_all('span', {'class': 'price-column'})[0].find('span', {'class': 'main-value'}).text
        cent = item.find_all('span', {'class': 'price-column'})[0].find_all('span', {'class': 'sub'})[1].text
        product_price = ('{}{}'.format(dollar, cent))
        product.product_price = product_price

        # Product Image
        image = item.find_all('img')[0].get('src')
        product.product_image = image

        # Price per serving
        try:
            prod_weight = re.findall(r"[-+]?\d*\.\d+|\d+", product_name)[-1]
            prod_weight = float(prod_weight)
            product_price = float(product_price)

            if float(prod_weight) > 100:
                pps = 999
            else:

                try:
                    pps = (format(product_price / prod_weight, '.2f'))
                except:
                    pps = 999
        except ValueError:
            pps = 999

        product.product_price_per_serving = pps

        # type of protein
        prod_type = "Vitamin"
        product.product_type = prod_type

        db.session.add(product)
        db.session.commit()

        rows_logged += 1

    print("logged {} rows".format(rows_logged))