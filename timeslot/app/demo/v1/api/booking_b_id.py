# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

import json
class BookingBId(Resource):

    def delete(self, b_id):

        return None, 204, None

def write_to_file(content):
    with open("./bookings.json", "w") as bookings:
        bookings.write(json.dumps(content))


def read_from_file():
    with open("./bookings.json", "r") as bookings:
        return json.loads(bookings.read())