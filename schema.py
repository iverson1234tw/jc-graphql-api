#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
#coding:utf-8

import graphene
from models import *
import schema_friends
from graphene_sqlalchemy import SQLAlchemyConnectionField

class Mutation(graphene.ObjectType):
    create_friend = schema_friends.CreateFriends.Field()

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    friend = graphene.List(schema_friends.FriendsObject, limit=graphene.Int(description='最大筆數'),
                                                        offset=graphene.Int(description='跳過筆數'),
                                                        id=graphene.Int(description='識別碼'),
                                                        name=graphene.String(description='名稱'),
                                                        gender=graphene.Int(description='性別(1:男 0:女)'),
                                                        height=graphene.String(description='身高(cm)'),
                                                        age=graphene.Int(description='年齡'),
                                                        distance=graphene.Int(description='距離(km)'))
    friendList = SQLAlchemyConnectionField(schema_friends.FriendsObject)
    def resolve_friend(self, info, **args):
        query = schema_friends.FriendsConnectionField.get_query(Friends, info, None, **args)
        return query.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
