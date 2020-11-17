# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

import json
class Booking(Resource):

    def get(self):
        # print(g.args)
        bookings = read_from_file()
        print(bookings)
        result = []
        final_result = {}
        for i in bookings:
            a = {}
            a["b_id"] = i
            a["dentistName"] = bookings[i]["dentistName"]
            a["patientName"] = bookings[i]["patientName"]
            a["timeslot"] = bookings[i]["timeslot"]
            result.append(a)
        # print(result)
        final_result["result"] = result
        print(final_result)
        return final_result, 200, None


    def post(self):
        print(g.json)
        bookings = read_from_file()
        print(bookings)
        print(g.json)

        ids = bookings.keys()
        id = [int(i) for i in ids]
        print(id)
        if len(id)==0:
            new_id=1000
        else:
            new_id = id[-1] + 1
        new_id = str(new_id)
        print(new_id, type(new_id))
        print(g.json['patientName'])
        bookings[new_id] = {"patientName": g.json['patientName'], "dentistName": g.json['dentistName'],"timeslot":g.json['timeslot']}
        print(bookings)
        write_to_file(bookings)
        return None, 201, None

def write_to_file(content):
    with open("./bookings.json", "w") as bookings:
        bookings.write(json.dumps(content))


def read_from_file():
    with open("./bookings.json", "r") as bookings:
        return json.loads(bookings.read())