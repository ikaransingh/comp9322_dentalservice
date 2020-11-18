import requests
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
