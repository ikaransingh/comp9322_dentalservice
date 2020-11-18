# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

import json
class BookingBId(Resource):

    def delete(self, b_id):
        bookings = read_from_file()
        print(bookings)
        b_id=str(b_id)
        ids = bookings.keys()
        id = [i for i in ids]
        if b_id in id:

            del bookings[b_id]
            print(bookings)
            write_to_file(bookings)

            return {"b_id":b_id},204,None

        else:

            return 	None, 400, None

def write_to_file(content):
    with open("./bookings.json", "w") as bookings:
        bookings.write(json.dumps(content))


def read_from_file():
    with open("./bookings.json", "r") as bookings:
        return json.loads(bookings.read())