import requests
from bs4 import BeautifulSoup
from database import session, Product


url = ['http://www.bodybuilding.com/store/mic.html',
       'http://www.bodybuilding.com/store/mic.html?pg=2',
       'http://www.bodybuilding.com/store/mic.html?pg=3']

for page in url:

    r = requests.get(page)
    soup = BeautifulSoup(r.content, "lxml")

    gen = soup.find_all('article', {'class': 'product-layout'})
    for item in gen:
        product = Product()
        # Dealer Name
        website = 'bodybuilding.com'
        product.product_dealer = website

        # Gets the product name
        prod = item.find_all('div', {'class': 'product-details'})[0].find_all('a')[0].text
        product.product_name = prod

        # Get Product Link
        href = item.find_all('h3')[0].find('a').get('href')
        link = 'https://bodybuilding.com%s' % href
        product.product_url = link

        # Get Product Price
        price = item.find_all('li', {'itemprop': 'price'})[0].text
        prod_price = price
        product.product_price = prod_price

        # Per Serving
        servings = item.find_all('li', {'class': 'product-spec'})[2].text[11:]
        # Price per serving
        try:
            pps = format(float(price[1:])/int(servings), '.2f')
            product.product_price_per_serving = pps
        except ValueError:
            product.product_price_per_serving = 'N/A'

        # type of protein
        prod_type = "Casein"
        product.product_type = prod_type

        # Product Image
        image = item.find_all('img')[0].get('src')
        prod_image = image
        product.product_image = prod_image

        session.add(product)
        session.commit()



