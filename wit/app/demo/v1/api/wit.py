import requests
from .credentials import WIT_TOKEN
from .dentist_api import get_dentists
from .dentist_api import get_dentists_info
from .timeslot_api import get_timeslot_info


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

        if json_result['intents'][0]['name'] == 'getDentistsInfo':
            dentistName = json_result['entities']['wit$contact:contact'][0]['body']
            print('Name detected: {}'.format(dentistName))
            answer = get_dentists_info(dentistName)

        if json_result['intents'][0]['name'] == 'getTimeslots':
            if json_result['entities']['wit$contact:contact'][0]['body'] in ['Dr. Oliver','Dr. Manish','Dr. Virdi']:
                dentistName=json_result['entities']['wit$contact:contact'][0]['body']
                print('Name detected: {}'.format(dentistName))
            answer = get_timeslot_info()
    except:
        answer = 'I do not understand :('
    return answer
