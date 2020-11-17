import requests
from .credentials import YELP_API_KEY

def get_timeslot_info():
    print('i am inside timeslots api get_timeslot_info WIT')
    result = requests.get('http://127.0.0.1:8085/v1/timeslots')
    print('i have got request result now')

    json_result = result.json()
    print(json_result)

    # print('i am inside dentist api get_dentists WIT')
    # print(json_result)
    # return f"The available dentists are {json_result['result'][0]['dentistName']}, " \
    #        f"{json_result['result'][1]['dentistName']}, and " \
    #        f"{json_result['result'][2]['dentistName']}"
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
