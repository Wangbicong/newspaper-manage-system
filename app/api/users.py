# -*-coding:utf8 -*-
from flask_restful import Resource
from app.models import User
from . import api


class UsersAPI(Resource):
    def get(self):
        return str(User.query.all())


class UserAPI(Resource):
    '''id为user的phone number'''
    def get(self, id):
        return 'user %r' % id


api.add_resource(UsersAPI, '/user/')
api.add_resource(UserAPI, '/user/<int:id>')