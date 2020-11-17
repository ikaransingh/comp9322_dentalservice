# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.timeslots import Timeslots
from .api.booking import Booking
from .api.booking_b_id import BookingBId


routes = [
    dict(resource=Timeslots, urls=['/timeslots'], endpoint='timeslots'),
    dict(resource=Booking, urls=['/booking'], endpoint='booking'),
    dict(resource=BookingBId, urls=['/booking/<int:b_id>'], endpoint='booking_b_id'),
]