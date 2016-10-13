import requests
from bs4 import BeautifulSoup

from ..extensions import db
from ..models import Product


def scrape_bodybuilding_casein():
    urls = ['http://www.bodybuilding.com/store/mic.html',
            'http://www.bodybuilding.com/store/mic.html?pg=2',
            'http://www.bodybuilding.com/store/mic.html?pg=3']

    rows_logged = 0
    for page in urls:

        r = requests.get(page)

        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "lxml")

            gen = soup.find_all('article', {'class': 'product-layout'})
            for item in gen:
                product = Product()
                # Dealer Name
                website = 'bodybuilding.com'
                product.product_dealer = website

                # Gets the product name
                prod = \
                    item.find_all('div', {'class': 'product-details'})[
                        0].find_all('a')
                if prod:

                    product.product_name = prod[0].text

                    # Get Product Link
                    href = item.find_all('h3')[0].find('a').get('href')
                    link = 'https://bodybuilding.com%s' % href
                    product.product_url = link

                    # Get Product Price
                    price = item.find_all('li', {'itemprop': 'price'})[0].text
                    prod_price = price
                    product.product_price = prod_price

                    # Per Serving
                    servings = item.find_all('li', {'class': 'product-spec'})[
                                   2].text[
                               11:]
                    # Price per serving
                    try:
                        pps = format(float(price[1:]) / int(servings), '.2f')
                        product.product_price_per_serving = pps
                    except ValueError:
                        product.product_price_per_serving = 'N/A'

                    # type of protein
                    prod_type = "Casein"
                    product.product_type = prod_type

                    # Product Image
                    image = item.find_all('img')[0].get('src')
                    prod_image = image
                    product.product_image = prod_image

                    try:
                        sale_item = item.find_all('div', {'class': 'violator'})[
                                        0].text[
                                    5:]
                        product.product_description = sale_item
                    except IndexError:
                        product.product_description = ''

                    db.session.add(product)
                    db.session.commit()

    print("logged {} rows".format(rows_logged))
    return
