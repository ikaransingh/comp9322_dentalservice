import requests


def cancel_booking(b_id):
    print('i am inside cancel_booking api WIT')
    print(f'delete {b_id}')
    result = requests.delete('http://127.0.0.1:8085/v1/booking/{}'.format(b_id))
    print('i have got request result now')
    # a=''.join(result)
    # print(a)
    print(result.status_code)

    if result.status_code==204:
        return f'Your booking has been cancelled. Booking id {b_id}.',204
    else:
        return 'No booking found with the provided booking id',400


def post_make_booking(dentistName,timeslot,patientName):
    print('i am inside post_make_booking api WIT')
    result = requests.get('http://127.0.0.1:8085/v1/timeslots')
    print('i have got request result now')

    json_result = result.json()
    print(json_result)

    result1 = requests.get('http://127.0.0.1:8085/v1/booking')
    print('i have got request result1 now')

    json_result1 = result1.json()
    print(json_result1)

    manish = [i for i in json_result['timeslot']]
    print(manish)
    virdi = [i for i in json_result['timeslot']]
    oliver = [i for i in json_result['timeslot']]

    for i in range(len(json_result1['result'])):
        if json_result1['result'][i]['dentistName'] == "Dr. Manish":
            manish.remove(json_result1['result'][i]['timeslot'])
        if json_result1['result'][i]['dentistName'] == "Dr. Virdi":
            virdi.remove(json_result1['result'][i]['timeslot'])
        if json_result1['result'][i]['dentistName'] == "Dr. Oliver":
            oliver.remove(json_result1['result'][i]['timeslot'])
    dict={}
    dict["Dr. Manish"] = manish
    dict["Dr. Virdi"] = virdi
    dict["Dr. Oliver"] = oliver
    print(dict)
    if dentistName in ['Dr. Oliver', 'Dr. Manish', 'Dr. Virdi']:
        if timeslot in dict[dentistName]:
            print('going to make booking now')
            result2 = requests.post('http://127.0.0.1:8085/v1/booking',json={
                "patientName": patientName,
                "dentistName": dentistName,
                "timeslot": timeslot
            })
            print('i have got request result2 now')

            json_result2 = result2.json()
            print(json_result2)
            return f" Congrats {json_result2['result'][0]['patientName']}! The booking is confirmed." \
                    f"The booking id is {json_result2['result'][0]['b_id']}. " \
                   f"Your dentist name is {json_result2['result'][0]['dentistName']}. " \
                   f"Your timeslot is {json_result2['result'][0]['timeslot']}. ",200
        else:
            return f"This timeslot {timeslot} is not available.",400
    else:
        return "Sorry, the dentist requested is not available.",400

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

