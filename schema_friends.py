#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
#coding:utf-8

import graphene
from models import *
from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class FriendsAttribute:
    name = graphene.String(description='名稱')
    gender = graphene.Int(description='性別(1:男, 0:女)')
    height = graphene.String(description='身高')
    age = graphene.Int(description='年齡')
    distance = graphene.Int(description='距離(km)')

class FriendsObject(SQLAlchemyObjectType):
    class Meta:
        model = Friends
        interfaces = (graphene.relay.Node,)

class FriendsConnectionField(SQLAlchemyConnectionField):
    def __init__(self, type, *args, **kwargs):
        super().__init__(type, name=String(), gender=Int(), height=String(), age=Int(), distance=Int(), *args, **kwargs)

    @classmethod
    def get_query(cls, model, info, sort=None, **args):
        query = super().get_query(model, info, None, **args)
        if 'limit' in args:
            query = query.limit(args['limit'])
        if 'offset' in args:
            query = query.offset(args['offset'])
        if 'id' in args:
            query = query.filter(Friends.id == args['id'])
        if 'name' in args:
            query = query.filter(Friends.name == args['name'])
        if 'gender' in args:
            query = query.filter(Friends.gender == args['gender'])
        if 'height' in args:
            query = query.filter(Friends.height == args['height'])
        if 'age' in args:
            query = query.filter(Friends.age == args['age'])
        if 'distance' in args:
            query = query.filter(Friends.distance == args['distance'])

        return query

class CreateFriends(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    gender = graphene.Int()
    height = graphene.String()
    age = graphene.Int()
    distance = graphene.Int()
    class Arguments:
        name = graphene.String()
        gender = graphene.Int()
        height = graphene.String()
        age = graphene.Int()
        distance = graphene.Int()
    def mutate(self, info, name, gender, height, age, distance):
        friend = Friends(name=name, gender=gender, height=height, age=age, distance=distance)
        db.session.add(friend)
        db.session.commit()
        return CreateFriends(id=friend.id, name=friend.name, gender=friend.gender, height=friend.height, age=friend.age, distance=friend.distance)






