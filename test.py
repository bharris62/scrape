import os
from amazon.api import AmazonAPI
import re


amazon = AmazonAPI('AKIAJ5ZUX3EZNSGONTQQ', 'p0mqBPGq+pD61TI4pILqza4F2o8SskZbLEeg4uZm', 'supps07-20')

prod = amazon.search(Keywords='preworkout', SearchIndex='All')
rows_logged = 0
count = 0
for i in prod:
    print(i.title)

