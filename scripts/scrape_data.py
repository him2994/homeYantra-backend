import requests
import gevent
from gevent import monkey
monkey.patch_all()
import json


def fetch_n_create(q):
	response = requests.request('GET', url + q)
	res = response.json()
	data = res['hits']
	for d in data:
		d['filters'] = json.dumps(d['filters'])
		response = requests.request('POST', 'http://localhost:8000/products/', data=d)
		print response.json()


url = 'https://gen.homeyantra.com/search/products?q='
data = ['refridgerator', 'air conditioner', 'microwave', 'television', 'washing machine']

jobs = []

for i in data:
	jobs.append(gevent.spawn(fetch_n_create, i))

gevent.joinall(jobs)

