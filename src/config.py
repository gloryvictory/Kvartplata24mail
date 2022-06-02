#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          : Viacheslav Zamaraev
#   email           : zamaraev@gmail.com
#   Script Name     : cfg.py
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

#FILE_CSV = str(time.strftime("%Y-%m-%d") + "_shp" + ".csv")
#CSV_DELIMITER = ';'

FILE_LOG_NAME = 'kvartplata24_logger'
FILE_LOG = str(strftime("%Y-%m-%d") + FILE_LOG_NAME + '.log')
FILE_LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
#sFILE_LOG_LEVEL = 'INFO'

SMTP_HOST = ''
SMTP_PORT =''
SMTP_USER = ''
SMTP_PASSWORD = ''

#DATABASE_NAME = 'gisdata'