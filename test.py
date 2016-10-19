import os
from amazon.api import AmazonAPI


key = os.environ['AMAZON_ACCESS_KEY']
secret = os.environ['AMAZON_SECRET_KEY']

amazon = AmazonAPI(key, secret, 'thenooacc-20')

product = amazon.search(Keywords='whey', SearchIndex='All')

count=0
for i in product:
    # print(dir(i))

    # description of product / Product Name
    print(i.title)

    # Price of Product
    print(i.price_and_currency[0])

    # Image of product
    print(i.medium_image_url)

    # offer url
    print(i.offer_url)

    # price per serving
    pps = 'currently unavail'

    product_dealer = 'Amazon'

    product_type = 'Whey'

    product_description = ''

    count += 1

print(count)

