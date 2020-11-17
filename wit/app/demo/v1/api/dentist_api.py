import requests
from .credentials import WEATHER_API_KEY
import json
def get_dentists():
    print('i am inside dentist api get_dentists WIT')
    result = requests.get('http://127.0.0.1:8080/v1/dentists')
    # print('i have got request result now')
    # print(result)
    json_result=result.json()
    # print(json_result['result'][0])

    # print('i am inside dentist api get_dentists WIT')
    print(json_result)
    return f"The available dentists are {json_result['result'][0]['dentistName']}, " \
           f"{json_result['result'][1]['dentistName']}, and " \
           f"{json_result['result'][2]['dentistName']}"

def get_dentists_info(dentistName):
    print('i am inside dentist api get_dentists_info WIT')
    result = requests.get('http://127.0.0.1:8080/v1/dentists/{}'.format(dentistName))
    # 'http://127.0.0.1:8080/v1/dentists/Dr.%20Virdi'
    print(result)
    json_result = result.json()
    print(json_result)
    if json_result!=None:
        return f"The dentist id is {json_result['result'][0]['d_id']}. " \
           f"His name is {json_result['result'][0]['dentistName']}. " \
           f"His specialization is {json_result['result'][0]['specialization']} and " \
           f"he lives in {json_result['result'][0]['location']}."
    else:
        return f"Sorry, {dentistName} does not work here"



def get_weather_info(location):
    result = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
                          .format(location, WEATHER_API_KEY))
    json_result = result.json()
    return f"It is {json_result['weather'][0]['description']} " \
           f"with max temperature of {json_result['main']['temp_max']} " \
           f"degree C and min temperature of {json_result['main']['temp_min']} " \
           f"degree C but feels like {json_result['main']['feels_like']} degree C. in {json_result['name']}"