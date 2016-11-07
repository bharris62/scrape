import requests
import json
import urllib



url = 'http://api.walmartlabs.com/v1/search?apiKey=5rjw69f2qeuvmcyr94tptvsd&lsPublisherId=li*LWdY/zkM&query=ipod&categoryId=3944&sort=price&order=asc'

r = requests.get(url)

