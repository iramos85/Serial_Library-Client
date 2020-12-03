
# import * means import everything from peewee

from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('killer_profiles.sqlite')

# http://docs.peewee-orm.com/en/latest/peewee/models.html

class User(UserMixin, Model):
    username=CharField(unique=True)
    email=CharField(unique=True)
    password=CharField()

    class Meta:
        database = DATABASE


class Killer(Model):
    # Columns
    name = CharField()
    active = CharField()
    summary = CharField()
    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    # Creating table when we're initializing
    DATABASE.create_tables([User, Killer], safe=True)
    print("TABLES Created")
    DATABASE.close()

