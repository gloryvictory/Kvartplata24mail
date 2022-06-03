#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          : Viacheslav Zamaraev
#   email           : zamaraev@gmail.com
#   Script Name     : main.py
#   Created         : 02.06.2022
#   Last Modified	: 02.06.2022
#   Version		    : 1.0
#   PIP             :
#   RESULT          :
# Modifications	: 1.1 -
# Description   : load data from Excel file and send to users by list pdf attachements
# @echo off

# C:\Glory\Projects\Python\Kvartplata24mail\data\Севастопольская

import os
from datetime import datetime

from core.logger import get_logger
import config

logger = get_logger()

def make_gui():
    #root.title('Рассылка расчетных листков Квартплата24')
    pass




def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    #make_gui()
    # root = Root()
#    root.mainloop()

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == "__main__":
    main()