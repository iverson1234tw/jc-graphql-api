# -*- coding: utf8 -*-
# coding: utf-8

from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from __init__ import db

class Friends(db.Model):
    __tablename__ = 'friends'

    id = db.Column('ID', db.BigInteger, primary_key=True)
    name = db.Column('Name', db.String(45))
    gender = db.Column('Gender', db.Integer)
    height = db.Column('Height', db.String(45))
    age = db.Column('Age', db.Integer)
    distance = db.Column('Distance', db.Integer)