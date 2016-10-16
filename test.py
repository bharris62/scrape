import requests
from bs4 import BeautifulSoup


urls = ['http://www.bodybuilding.com/store/mic.html',
        'http://www.bodybuilding.com/store/mic.html?pg=2',
        'http://www.bodybuilding.com/store/mic.html?pg=3']

rows_logged = 0
for page in urls:

    r = requests.get(page)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "lxml")

        gen = soup.find_all('article', {'class': 'product-layout'})
        for item in gen:

            # Dealer Name
            website = 'bodybuilding.com'
            print(website)

            # Gets the product name
            prod = \
                item.find_all('div', {'class': 'product-details'})[
                    0].find_all('a')
            if prod:

                print(prod[0].text)

                # Get Product Link
                href = item.find_all('h3')[0].find('a').get('href')
                link = 'https://bodybuilding.com%s' % href
                print(link)

                # Get Product Price
                try:
                    price = item.find_all('li', {'itemprop': 'price'})[0].text
                    prod_price = price
                    print(prod_price)
                except IndexError:
                    print('N/A')

                # Per Serving
                servings = item.find_all('li', {'class': 'product-spec'})[
                               2].text[
                           11:]
                # Price per serving
                try:
                    pps = format(float(price[1:]) / int(servings), '.2f')
                    print(pps)
                except ValueError:
                    print('N/A')

                # type of protein
                prod_type = "Casein"
                print(prod_type)

                # Product Image
                image = item.find_all('img')[0].get('src')
                prod_image = image
                print(prod_image)

                try:
                    sale_item = item.find_all('div', {'class': 'violator'})[
                                    0].text[
                                5:]
                    print(sale_item)
                except IndexError:
                    print('no sale')


                rows_logged += 1

print(rows_logged)