import requests
from .credentials import WIT_TOKEN
from .dentist_api import get_dentists
from .timeslot_api import get_yelp_info


def wit(expression):
    answer = ''
    try:
        result = requests.get('https://api.wit.ai/message?v=20201117&q={}'.format(expression),
                              headers={'Authorization': WIT_TOKEN})
        json_result = result.json()
        print(json_result)
        if json_result['intents'][0]['name'] == 'getDentists':
            
            print('i am calling get_dentists()')
            answer = get_dentists()
        # if json_result['intents'][0]['name'] == 'GetRestaurants':
        #     location = json_result['entities']['wit$location:location'][0]['body']
        #     print('location detected: {}'.format(location))
        #     answer = get_yelp_info(location)
    except:
        answer = 'I do not understand :('
    return answer
