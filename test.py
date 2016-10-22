import requests
from bs4 import BeautifulSoup
import re


urls = ['http://www.bodybuilding.com/store/mic.html',
        'http://www.bodybuilding.com/store/mic.html?pg=2',
        'http://www.bodybuilding.com/store/mic.html?pg=3']

for page in urls:

    r = requests.get(page)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "lxml")

        gen = soup.find_all('article', {'class': 'product-layout'})
        for item in gen:

            # Gets the product name
            prod = \
                item.find_all('div', {'class': 'product-details'})[
                    0].find_all('a')
            if prod:

                product_name = prod[0].text

                prod_weight = re.findall(r"[-+]?\d*\.\d+|\d+", product_name)[-1]
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

                print(pps)




