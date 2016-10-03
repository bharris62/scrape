import requests
from bs4 import BeautifulSoup
from database import session, Product


url = 'http://www.bodybuilding.com/store/protein-powder.html'
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

gen = soup.find_all('article', {'class': 'product-layout'})

for item in gen:
    # Dealer Name
    product_dealer = 'bodybuilding.com'
    product_dealer = Product(product_dealer=product_dealer)
    session.add(product_dealer)

    # Gets the product name
    product_name = item.find_all('div', {'class': 'product-details'})[0].find_all('a')[0].text
    product_name = Product(product_name=product_name)
    session.add(product_name)

    # Get Product Link
    href = item.find_all('h3')[0].find('a').get('href')
    product_link = 'https://bodybuilding.com%s' % href
    product_link = Product(product_url=product_link)
    session.add(product_link)

    # Get Product Price
    price = item.find_all('li', {'itemprop': 'price'})[0].text
    product_price = price
    product_price = Product(product_price=product_price)
    session.add(product_price)

    # Per Serving
    servings = item.find_all('li', {'class': 'product-spec'})[2].text[11:]
    # Price per serving
    product_price_per_serving = format(float(price[1:])/int(servings), '.2f')
    product_price_per_serving = Product(product_price_per_serving=product_price_per_serving)
    session.add(product_price_per_serving)
    # type of protein
    product_type = "Whey"
    product_type = Product(product_type=product_type)
    session.add(product_type)
    # Product Image
    image = item.find_all('img')[0].get('src')
    product_image = image
    product_image = Product(product_image=product_image)
    session.add(product_image)

    session.commit()
    break



