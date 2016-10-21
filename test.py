import os
from amazon.api import AmazonAPI


amazon = AmazonAPI('AKIAIJHUEBHIPCLQ7KLQ', 'xs7YIeB4oR6/QvXY7DCbvFhCxbGIJx4EeUqMEwMy', 'thenooacc-20')

product = amazon.search(Keywords='preworkout', SearchIndex='All')

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

