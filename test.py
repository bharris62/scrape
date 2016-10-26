from amazon.api import AmazonAPI


amazon = AmazonAPI('AKIAJ5ZUX3EZNSGONTQQ', 'p0mqBPGq+pD61TI4pILqza4F2o8SskZbLEeg4uZm', 'supps07-20')

prod = amazon.search(Keywords='multivitamin', SearchIndex='All')

for i in prod:
    print(i.title)