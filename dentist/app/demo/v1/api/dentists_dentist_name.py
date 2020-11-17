# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
import json
from . import Resource
from .. import schemas


class DentistsDentistName(Resource):

    def get(self, dentist_name):

        return {}, 200, None


def write_to_file(content):
    with open("./dentists.json", "w") as dentists:
        dentists.write(json.dumps(content))


def read_from_file():
    with open("./dentists.json", "r") as dentists:
        return json.loads(dentists.read())