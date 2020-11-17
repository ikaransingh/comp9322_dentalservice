# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import json

class Timeslots(Resource):

    def get(self):
        timeslots = read_from_file()

        print(timeslots['timeslots'])
        i= timeslots['timeslots'].split(',')
        print(i)
        result={}
        result['timeslot']=i

        # a=timeslots.split
        return result, 200, None

def write_to_file(content):
    with open("./timeslots.json", "w") as timeslots:
        timeslots.write(json.dumps(content))


def read_from_file():
    with open("./timeslots.json", "r") as timeslots:
        return json.loads(timeslots.read())