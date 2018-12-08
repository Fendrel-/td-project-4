from peewee import *
from datetime import datetime

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

    def New():
        date = datetime.today()
        employee_name = input('\n What is your name?: ')
        task_name = input(' What do you want to call this task?: ')
        time_spent = input(' How many minutes did you spend on this?: ')
        notes = input(' Enter additional notes (optional): ')
        Entry.create(date=date,
                     employee_name=employee_name,
                     task_name=task_name,
                     time_spent=time_spent,
                     notes=notes)

    def Display():
        pass

    def Delete():
        pass

    def Edit():
        pass
