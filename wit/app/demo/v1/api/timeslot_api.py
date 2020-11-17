import requests
from .credentials import YELP_API_KEY


def get_yelp_info(location):
    result = requests.get('https://api.yelp.com/v3/businesses/search?term=restaurant&location={}'
                          .format(location),
                          headers={'Authorization': YELP_API_KEY})
    json_result = result.json()
    result = []
    for r in json_result['businesses']:
        if r['name'] and r['phone']:
            row = f'{r["name"]} | {r["phone"]}'
            result.append(row)
    return ', '.join(result[:10])
