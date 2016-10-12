import requests
from bs4 import BeautifulSoup


url = 'http://www.vitaminshoppe.com/c/whey-protein-isolate/N-8eb'

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

gen = soup.find_all('div', {'class': 'listing'})

for item in gen:
    # Get the product name
    # print(item.find_all('span', {'itemprop': 'name'})[0].text)

    # Get Product Link
    # url_ext = item.find_all('a', {'class': 'gray-link'})[0].get('href')
    # print('www.vitaminshoppe.com%s' %url_ext)

    # Product Image
    # print(item.find_all('img')[0].get('src'))

    # Get Product Price
    # dollar = item.find_all('span', {'class': 'price-column'})[0].find('span', {'class': 'main-value'}).text
    # cent = item.find_all('span', {'class': 'price-column'})[0].find_all('span', {'class': 'sub'})[1].text

    # type of protein
    prod_type = "Whey"
    # product.product_type = prod_type

    # TODO Price per serving
    pps = item.find_all('li', {'class': 'product-description'})[0].find('a').get('href')
    url = 'http://vitaminshoppe.com%s' %pps

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    # very slow, but operable
    price_per_serving = soup.find_all('p', {'class': 'mtop5'})[4].text[23:27]
    print(price_per_serving)
