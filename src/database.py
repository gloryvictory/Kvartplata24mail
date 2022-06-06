import os.path

from peewee import *

import config as cfg


db = SqliteDatabase(cfg.DATABASE_NAME)


class Person(Model):
    # Тип адреса улицы
    street_type = CharField(max_length=255, default="")
    street = CharField(max_length=255, default="")              # Улица
    home = CharField(max_length=255, default="")                # Дом
    # Тип адреса Квартира
    flat_type = CharField(max_length=255, default="")
    flat = CharField(max_length=255, default="")                # Квартира
    room = CharField(max_length=255, default="")                # Комната
    # Номер лицевого счета
    lic_id = CharField(max_length=255, default="")
    surname = CharField(max_length=255, default="")             # Фамилия
    name = CharField(max_length=255, default="")                # Имя
    middlename = CharField(max_length=255, default="")          # Отчество
    email = CharField(max_length=255, default="")               # E-mail
    human_id = CharField(max_length=255, default="")            # ID человека

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'
        db_table = 'Person'

    # is_relative = BooleanField()
    #created = peewee.DateField(default=datetime.date.today)
    # create_time = DateTimeField(default=datetime.now)
    # update_time = DateTimeField(default=datetime.now)


class Files(Model):
    # Полный путь к файлу
    file_name = CharField(max_length=255, default="")
    street_type = CharField(max_length=255, default="")     # Тип адреса улицы
    street = CharField(max_length=255, default="")          # Улица
    home = CharField(max_length=255, default="")            # Дом
    # Тип адреса Квартира
    flat_type = CharField(max_length=255, default="")
    flat = CharField(max_length=255, default="")            # Квартира
    room = CharField(max_length=255, default="")            # Комната
    # Номер лицевого счета
    lic_id = CharField(max_length=255, default="")
    year = CharField(max_length=255, default="")            # Год выгрузки
    month = CharField(max_length=255, default="")           # Месяц выгрузки

    class Meta:
        database = db  # модель будет использовать базу данных 'people.db'
        db_table = 'Files'
