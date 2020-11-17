# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

from .wit import wit
class Chat(Resource):

    def get(self):
        print(g.args)
        answer = wit(g.args['expression'])

        return {'answer': answer}, 200, None