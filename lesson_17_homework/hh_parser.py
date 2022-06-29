import requests
import pprint

DOMAIN = 'https://api.hh.ru/'
urls_list = f'{DOMAIN}vacancies/'
params = {
    'page': '1'
}
res = requests.get(urls_list, params = params)
pprint.pprint(res.json())
