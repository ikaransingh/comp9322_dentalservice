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
            value=json_result['entities']['wit$contact:contact'][0]['body']
            if value in ['Dr. Oliver','Dr. Manish','Dr. Virdi']:
                dentistName=value
                print('Name detected: {}'.format(dentistName))
                intermediate = get_timeslot_info()
                answer=f"The available timeslots of {dentistName} are {intermediate[dentistName]}"
            else:
                intermediate = get_timeslot_info()
                value1="Dr. Manish"
                value2="Dr. Virdi"
                value3="Dr. Oliver"
                
                answer = f"The available timeslots of {value1} are {intermediate[value1]}. " \
                         f"The available timeslots of {value2} are {intermediate[value2]}. " \
                         f"The available timeslots of {value3} are {intermediate[value3]}. "



    except:
        answer = 'I do not understand :('
    return answer
