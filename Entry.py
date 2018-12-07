from peewee import *

db = SqliteDatabase('entries.db')


class BaseModel(Model):
    class Meta:
        database = db


class Entry(BaseModel):
    date = DateTimeField()
    employee_name = CharField()
    task_name = CharField()
    time_spent = IntegerField()
    notes = TextField()
