import os
from ..extensions import db
from ..models import Product
from amazon.api import AmazonAPI


def scrape_whey_amazon():
    product = Product()

    amazon = AmazonAPI(os.environ['AMAZON_ACCESS_KEY'], os.environ['AMAZON_SECRET_KEY'], 'thenooacc-20')

    prod = amazon.search(Keywords='whey', SearchIndex='All')
    rows_logged = 0
    for i in prod:
        # print(dir(i))

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

        # price per serving
        pps = 'currently unavail'
        product.product_price_per_serving = pps

        website = 'Amazon'
        product.product_dealer = website

        prod_type = 'Whey'
        product.product_type = prod_type

        prod_description = ''
        product.product_description = prod_description

        count += 1

        db.session.add(product)
        db.session.commit()

    print("logged {} rows".format(rows_logged))