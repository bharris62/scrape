import requests
from bs4 import BeautifulSoup


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
                product_manufacturer = prod[0].text.split()[0]

                print(product_name)
                print(product_manufacturer)

                break