from peewee import *


db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'
        db_table = 'Person'
