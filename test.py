import requests
from bs4 import BeautifulSoup

import re


url = 'http://www.vitaminshoppe.com/c/whey-protein-isolate/N-8eb'

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

rows_logged = 0

gen = soup.find_all('div', {'class': 'listing'})

for item in gen:

    # Get the product name
    product_name = item.find_all('span', {'itemprop': 'name'})[0].text
    product_name = product_name


    # Get Product Price
    dollar = item.find_all('span', {'class': 'price-column'})[0].find('span', {'class': 'main-value'}).text
    cent = item.find_all('span', {'class': 'price-column'})[0].find_all('span', {'class': 'sub'})[1].text
    product_price = ('{}{}'.format(dollar, cent))
    product_price = product_price

    try:
        prod_weight = re.findall(r"[-+]?\d*\.\d+|\d+", product_name)[-1]
        print(prod_weight)
        print(product_price)
        prod_weight = float(prod_weight)
        product_price = float(product_price)

        if float(prod_weight) > 11:
            pps = 999
        else:

            try:
                pps = (format(product_price / prod_weight, '.2f'))
            except:
                pps = 999
    except ValueError:
        pps = 999
    print(product_name)
    print(pps)
