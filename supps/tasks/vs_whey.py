import requests
from bs4 import BeautifulSoup

from supps.models import Product
from ..extensions import db


def scrape_vitamin_shoppe_whey():
    url = 'http://www.vitaminshoppe.com/c/whey-protein-isolate/N-8eb'

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
        link = 'www.vitaminshoppe.com%s' % url_ext
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
        pps = item.find_all('li', {'class': 'product-description'})[0].find('a').get('href')
        url = 'http://vitaminshoppe.com%s' % pps
        product.product_url = url

        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")

        # very slow, but operable
        price_per_serving = soup.find_all('p', {'class': 'mtop5'})[4].text[23:27]
        product.product_price_per_serving = price_per_serving

        # type of protein
        prod_type = "Whey"
        product.product_type = prod_type


        db.session.add(product)
        db.session.commit()

        rows_logged += 1

    print("logged {} rows".format(rows_logged))
