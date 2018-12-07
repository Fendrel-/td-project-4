from peewee import *

db = SqliteDatabase('entries.db')


class BaseModel(Model):
    class Meta:
        database = db
