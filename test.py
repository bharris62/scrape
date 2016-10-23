import os
from amazon.api import AmazonAPI
import re


amazon = AmazonAPI('AKIAIJHUEBHIPCLQ7KLQ', 'xs7YIeB4oR6/QvXY7DCbvFhCxbGIJx4EeUqMEwMy', 'thenooacc-20')

prod = amazon.search(Keywords='preworkout', SearchIndex='All')
rows_logged = 0
count = 0
for i in prod:
    print(i.title)
