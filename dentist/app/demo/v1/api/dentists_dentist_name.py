# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
import json
from . import Resource
from .. import schemas


class DentistsDentistName(Resource):

    def get(self, dentist_name):
        print(dentist_name)
        dentists = read_from_file()
        print(dentists)
        result=[]
        final_result = {}
        for i in dentists:
            a = {}
            a["d_id"] = i
            a["dentistName"] = dentists[i]["dentistName"]
            a["specialization"] = dentists[i]["specialization"]
            a["location"] = dentists[i]["location"]
            if a["dentistName"]==dentist_name:

                result.append(a)
        print(result)
        if len(result)==0:

            return None, 404, None
        else:
            final_result["result"] = result
            return final_result, 200, None


def write_to_file(content):
    with open("./dentists.json", "w") as dentists:
        dentists.write(json.dumps(content))


def read_from_file():
    with open("./dentists.json", "r") as dentists:
        return json.loads(dentists.read())