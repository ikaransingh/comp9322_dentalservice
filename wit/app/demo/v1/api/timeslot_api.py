import requests
from .credentials import YELP_API_KEY

def get_timeslot_info():
    print('i am inside timeslots api get_timeslot_info WIT')
    result = requests.get('http://127.0.0.1:8085/v1/timeslots')
    print('i have got request result now')

    json_result = result.json()
    print(json_result)

    result1 = requests.get('http://127.0.0.1:8085/v1/booking')
    print('i have got request result1 now')

    json_result1 = result1.json()
    print(json_result1)

    manish=[i for i in json_result['timeslot']]
    print(manish)
    virdi=[i for i in json_result['timeslot']]
    oliver=[i for i in json_result['timeslot']]

    for i in range(len(json_result1['result'])):
        if json_result1['result'][i]['dentistName']=="Dr. Manish":
            manish.remove(json_result1['result'][i]['timeslot'])
        if json_result1['result'][i]['dentistName']=="Dr. Virdi":
            virdi.remove(json_result1['result'][i]['timeslot'])
        if json_result1['result'][i]['dentistName']=="Dr. Oliver":
            oliver.remove(json_result1['result'][i]['timeslot'])

    print(virdi)
    dict={}
    dict["Dr. Manish"]=(', ').join(manish)
    dict["Dr. Virdi"]=(', ').join(virdi)
    dict["Dr. Oliver"]=(', ').join(oliver)

    print(dict)
    return dict
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
