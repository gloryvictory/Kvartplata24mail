#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          : Viacheslav Zamaraev
#   email           : zamaraev@gmail.com
#   Script Name     : config.py
#   Created         : 02.06.2022
#   Last Modified	: 02.06.2022
#   Version		    : 1.0
#   PIP             :
#   RESULT          :
# Modifications	: 1.1 -
# Description   :
# @echo off

from time import strftime   # Load just the strftime Module from Time

FOLDER_OUT_WIN = ''
FOLDER_DATA = 'C:\\Glory\\Projects\\Python\\Kvartplata24mail\\data\\'


FILE_LOG_NAME = 'kvartplata24'
FILE_LOG = str(strftime("%Y-%m-%d") + '_' + FILE_LOG_NAME + '.log')
FILE_LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
#DATABASE_NAME = str(strftime("%Y-%m-%d") + '_' + FILE_LOG_NAME + '.db')
DATABASE_NAME = 'people.db'

EXCEL_SHEET_NAME = 'Персональные данные'

SMTP_HOST = 'smtp.mail.ru'
SMTP_PORT = '465'
SMTP_USER = 'kvartplata2472@mail.ru'
SMTP_PASSWORD = '8EqamG3x9Mv8ktpnksKm'


#FILE_CSV = str(time.strftime("%Y-%m-%d") + "_shp" + ".csv")
#CSV_DELIMITER = ';'
#sFILE_LOG_LEVEL = 'INFO'
