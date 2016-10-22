import os

from amazon.api import AmazonAPI
import re

amazon = AmazonAPI('AKIAIJHUEBHIPCLQ7KLQ', 'xs7YIeB4oR6/QvXY7DCbvFhCxbGIJx4EeUqMEwMy', 'thenooacc-20')

prod = amazon.search(Keywords='whey', SearchIndex='All')

for i in prod:
    prod_weight = re.findall(r"[-+]?\d*\.\d+|\d+", i.title)[-1]
    price = i.price_and_currency[0]
    print(price)

    try:
        if float(prod_weight) > 11:
            pps = 999
        else:
            try:
                pps = format(float(price) / float(prod_weight), '.2f')
            except TypeError:
                pps = 999

        print(pps)

    except ValueError:
        pass