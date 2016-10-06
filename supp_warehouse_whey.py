import requests
from bs4 import BeautifulSoup
from database import session, Product


url = ['http://www.supplementwarehouse.com/protein/whey-isolate-protein.html?p=1',
       'http://www.supplementwarehouse.com/protein/whey-isolate-protein.html?p=2',
       'http://www.supplementwarehouse.com/protein/whey-isolate-protein.html?p=3']

rows_logged = 0
for page in url:

    r = requests.get(page)
    soup = BeautifulSoup(r.content, "lxml")

    gen = soup.find_all('article', {'class': 'product-layout'})
    for item in gen:

        product = Product()

        # Dealer Name
        website = 'Supplement Warehouse'
        # product.product_dealer = website

        # TODO Get the product name

        # TODO Get Product Link

        # TODO Get Product Price

        # TODO Per Serving

        # TODO Price per serving

        # type of protein
        prod_type = "Whey"
        # product.product_type = prod_type

        # TODO Product Image

        session.add(product)
        session.commit()


print("logged {} rows".format(rows_logged))