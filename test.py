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
    dollar = item.find_all('span', {'class': 'price-column'})[0].find('span', {'class': 'main-value'}).text
    cent = item.find_all('span', {'class': 'price-column'})[0].find_all('span', {'class': 'sub'})[1].text



    # TODO Per Serving

    # TODO Price per serving

    # type of protein
    prod_type = "Whey"
    # product.product_type = prod_type


    break
