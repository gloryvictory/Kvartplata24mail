import logging
import os.path
from peewee import *
import pandas as pd

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


def excel_to_db(file_excel_full_path = ''):
    if not os.path.isfile(file_excel_full_path):
        msg_str = f"file doesn't  exist {file_excel_full_path}"
        logging.info(msg_str)
        print(msg_str)

    if os.path.isfile(file_excel_full_path):
        one_person = Person()
        #one_person.truncate_table()
        one_person.create_table()
        # Load the xlsx file
        excel_data = pd.read_excel(file_excel_full_path,  sheet_name= cfg.EXCEL_SHEET_NAME)
        # Read the values of the file in the dataframe
        data = pd.DataFrame(excel_data)
        print(data.columns)
        # print(data.columns.ravel())
        #print(data.head())
        print(data.count()) # выводит статистику по файлу Excel

        for index, row in data.iterrows():
            tmp_str = str(row['E-mail'])
            # Выбираем всех, у кого есть почта
            if len(tmp_str) > 4 :
                one_person = Person()
                print(row['E-mail'], row['Имя'])
                one_person.street_type = row['Тип адреса улицы']
                one_person.street = row['Улица']
                one_person.home = row['Дом']
                one_person.flat_type = row['Тип адреса Квартира']
                one_person.flat = row['Квартира']
                one_person.room = row['Комната']
                one_person.lic_id = row['Номер лицевого счета']
                one_person.surname = row['Фамилия']
                one_person.name = row['Имя']
                one_person.middlename = row['Отчество']
                one_person.email = row['E-mail']
                one_person.human_id = row['ID человека']
                one_person.save()

        # Print the content
        # print("The content of the file is:\n", data)