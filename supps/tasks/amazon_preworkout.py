import os
from ..extensions import db
from ..models import Product
from amazon.api import AmazonAPI
import re


def scrape_preworkout_amazon():

    amazon = AmazonAPI('AKIAIJHUEBHIPCLQ7KLQ', 'xs7YIeB4oR6/QvXY7DCbvFhCxbGIJx4EeUqMEwMy', 'thenooacc-20')

    prod = amazon.search(Keywords='preworkout', SearchIndex='All')
    rows_logged = 0
    for i in prod:
        product = Product()
        # product manufacturer
        prod_manufacturerer = i.publisher
        product.product_manufacturer = prod_manufacturerer

        # description of product / Product Name
        prod_name = i.title
        product.product_name = prod_name

        # Price of Product
        prod_price = i.price_and_currency[0]
        product.product_price = prod_price

        # Image of product
        image = i.medium_image_url
        product.product_image = image

        # offer url
        url = i.offer_url
        product.product_url = url

        website = 'Amazon'
        product.product_dealer = website

        prod_type = 'Pre-Workout'
        product.product_type = prod_type

        prod_description = ''
        product.product_description = prod_description


        try:
            try:
                prod_weight = re.findall(r"[-+]?\d*\.\d+|\d+", prod_name)[-1]
            except IndexError:
                prod_weight = 1
            if float(prod_weight) > 100:
                pps = 1
            else:
                try:
                    pps = format(float(prod_price) / float(prod_weight), '.2f')
                except TypeError:
                    pps = 1

            product.product_price_per_serving = pps

        except ValueError:
            product.product_price_per_serving = pps


        rows_logged += 1
        db.session.add(product)
        db.session.commit()

    print("logged {} rows".format(rows_logged))