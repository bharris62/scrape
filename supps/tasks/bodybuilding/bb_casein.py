import requests
from bs4 import BeautifulSoup
import re

from supps.extensions import db
from supps.models import Product


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
                    prod_desc = prod[0].text
                    product.product_name = prod[0].text
                    try:
                        product.product_manufacturer = prod[0].text.split()[0]
                    except:
                        product.product_manufacturer = ':('

                    # Get Product Link
                    href = item.find_all('h3')[0].find('a').get('href')
                    link = 'https://bodybuilding.com%s' % href
                    product.product_url = link

                    # Get Product Price
                    try:
                        price = item.find_all('li', {'itemprop': 'price'})[0].text
                        prod_price = price
                        product.product_price = prod_price
                    except IndexError:
                        product.product_price = 'N/A'
                    # Per Serving
                    servings = item.find_all('li', {'class': 'product-spec'})[
                                   2].text[
                               11:]
                    # Price per serving
                    try:
                        prod_weight = re.findall(r"[-+]?\d*\.\d+|\d+", prod_desc)[-1]
                        try:
                            price = item.find_all('li', {'itemprop': 'price'})[0].text
                        except:
                            price = 1

                        if float(prod_weight) > 11:
                            pps = 999
                        else:

                            try:
                                pps = format(float(price[1:]) / float(prod_weight), '.2f')
                            except TypeError:
                                pps = 999

                        product.product_price_per_serving = pps

                    except ValueError:
                        product.product_price_per_serving = 'N/A'

                    # type of protein
                    prod_type = "Protein"
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
                    rows_logged +=1

    print("logged {} rows".format(rows_logged))
    return
