import requests
from bs4 import BeautifulSoup

url = 'http://www.vitaminshoppe.com/c/pre-workout-formulas/N-8f7'

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

rows_logged = 0

gen = soup.find_all('div', {'class': 'listing'})

for item in gen:

    # Dealer Name
    website = 'Vitamin Shoppe'
    product_dealer = website

    # Get the product name
    product_name = item.find_all('span', {'itemprop': 'name'})[0].text
    product_name = product_name

    # Get product manufacturer
    prod_manufacturer = item.find_all('span', {'itemprop': 'brand'})[0].text
    product_manufacturer = prod_manufacturer.split()[0]

    # Get Product Link
    url_ext = item.find_all('a', {'class': 'gray-link'})[0].get('href')
    link = 'www.vitaminshoppe.com%s' % url_ext
    product_url = link

    print(product_url)

    break

