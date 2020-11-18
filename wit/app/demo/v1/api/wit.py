import requests
from .credentials import WIT_TOKEN
from .dentist_api import get_dentists
from .dentist_api import get_dentists_info
from .timeslot_api import get_timeslot_info
from .timeslot_api import post_make_booking
from .timeslot_api import cancel_booking
import json

def wit(expression,patientName):
    answer = ''
    try:
        patientName=''
        result = requests.get('https://api.wit.ai/message?v=20201118&q={}'.format(expression),
                              headers={'Authorization': WIT_TOKEN})
        json_result = result.json()
        print(json_result)

        if json_result['intents'][0]['name'] == 'yes':
            userinfo=read_from_file()
            if 'makeBooking' in userinfo:
                print('i am here bro')
                book=userinfo['makeBooking']
                print('hello',book)
                answer,code = post_make_booking(book[0],book[1],book[2])
                print(answer)
                del userinfo['makeBooking']
                write_to_file(userinfo)


            elif 'cancelBooking' in userinfo:
                b_id=userinfo['cancelBooking']
                answer,code = cancel_booking(b_id)

                del userinfo['cancelBooking']
                write_to_file(userinfo)

            else:
                answer='I do not understand :('


        if json_result['intents'][0]['name'] == 'postGreeting':
            userinfo=read_from_file()
            patientName = json_result['entities']['wit$contact:contact'][0]['body']
            dict={}
            dict["patientName"]=patientName
            print('i am calling post greeting()')
            write_to_file(dict)
            # answer = get_dentists()

            answer=f"Thanks {patientName}. I hope you are looking for available dentists to book appointment"

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


        if json_result['intents'][0]['name'] == 'makeBooking':
            value = json_result['entities']['wit$contact:contact'][0]['body']
            time = json_result['entities']['wit$datetime:datetime'][0]['body']
            timeslot=time.split(' ')[-1]
            print(timeslot)
            if value in ['Dr. Oliver', 'Dr. Manish', 'Dr. Virdi']:
                dentistName = value
                print('Name detected: {}'.format(dentistName))

            answer = "enter yes to confirm your booking"
            userinfo = read_from_file()
            if "patientName" in userinfo:
                patientName=userinfo["patientName"]
            userinfo["makeBooking"]=[dentistName,timeslot,patientName]

            if 'cancelBooking' in userinfo:
                del userinfo['cancelBooking']
            write_to_file(userinfo)


        if json_result['intents'][0]['name'] == 'cancelBooking':
            b_id = json_result['entities']['wit$number:number'][0]['body']
            b_id=int(b_id)
            userinfo = read_from_file()
            # inter,code = cancel_booking(b_id)
            answer = "enter yes to cancel your booking"
            userinfo["cancelBooking"] = b_id


            if 'makeBooking' in userinfo:
                del userinfo['makeBooking']
            write_to_file(userinfo)

    except:
        answer = 'I do not understand :('
    return answer

def write_to_file(content):
    with open("./userinfo.json", "w") as userinfo:
        userinfo.write(json.dumps(content))


def read_from_file():
    with open("./userinfo.json", "r") as userinfo:
        return json.loads(userinfo.read())