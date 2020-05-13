# -*- coding: utf8 -*-
# coding: utf8

####################
### Import Class ###
####################

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
import pymysql

app = Flask(__name__) #--- app initialization ---#

#################
### Setup app ###
#################

app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ee4821251@127.0.0.1/JCDatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = False

pymysql.install_as_MySQLdb()

db = SQLAlchemy(app)

CORS(app)
