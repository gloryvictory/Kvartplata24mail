
import os.path
from peewee import *

# import logging
# import pandas as pd

import config as cfg


#db = SqliteDatabase('people.db')
db = SqliteDatabase(cfg.DATABASE_NAME)


class Person(Model):
    street_type = CharField(max_length=255, default="")         # Тип адреса улицы
    street = CharField(max_length=255, default="")              # Улица
    home = CharField(max_length=255, default="")                # Дом
    flat_type = CharField(max_length=255, default="")           # Тип адреса Квартира
    flat = CharField(max_length=255, default="")                # Квартира
    room = CharField(max_length=255, default="")                # Комната
    lic_id = CharField(max_length=255, default="")              # Номер лицевого счета
    surname = CharField(max_length=255, default="")             # Фамилия
    name = CharField(max_length=255, default="")                # Имя
    middlename = CharField(max_length=255, default="")          # Отчество
    email = CharField(max_length=255, default="")               # E-mail
    human_id = CharField(max_length=255, default="")            # ID человека
    # is_relative = BooleanField()
    #created = peewee.DateField(default=datetime.date.today)
    # create_time = DateTimeField(default=datetime.now)
    # update_time = DateTimeField(default=datetime.now)
    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'
        db_table = 'Person'


class Files(Model):
    file_name = CharField(max_length=255, default="")  # Полный путь к файлу
    street_type = CharField(max_length=255, default="")  # Тип адреса улицы
    street = CharField(max_length=255, default="")  # Улица
    home = CharField(max_length=255, default="")  # Дом
    flat_type = CharField(max_length=255, default="")  # Тип адреса Квартира
    flat = CharField(max_length=255, default="")  # Квартира
    room = CharField(max_length=255, default="")  # Комната
    lic_id = CharField(max_length=255, default="")  # Номер лицевого счета
    year = CharField(max_length=255, default="")  # Год выгрузки
    month = CharField(max_length=255, default="")  # Месяц выгрузки


    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'
        db_table = 'Files'
