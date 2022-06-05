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
import sys
import logging
from datetime import datetime
# from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QListWidgetItem)

from peewee import *
from database import Person
from database import db as db_sqlite

from ui.main_form import Ui_frmMain


import config as cfg



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmMain()
        self.ui.setupUi(self)
        self.folder_excel_fullpath = ''         # полный путь к файлу Excel
        self.folder_base = ''                   # папка с Excel
        self.folder_pdf = ''                    #папка с pdf файлами



        self.ui.btnExcel.clicked.connect(self.open_file_excel)

        # self.set_logger()

    # def set_logger(self):
    #     for handler in logging.root.handlers[:]:  # Remove all handlers associated with the root logger object.
    #         logging.root.removeHandler(handler)
    #     # dir_out = get_output_directory()
    #     # file_log = str(os.path.join(dir_out, cfg.file_log))  # from cfg.file
    #     file_log = cfg.FILE_LOG
    #     if os.path.isfile(file_log):  # Если выходной LOG файл существует - удаляем его
    #         os.remove(file_log)
    #     logging.basicConfig(filename=file_log, format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO,
    #                         filemode='w')
    #     logging.info(file_log)


    def open_file_excel(self):
        # self.folder_data = cfg.FOLDER_DATA
        folder_data_start = ''
        if os.path.isdir(cfg.FOLDER_DATA):
            folder_data_start = cfg.FOLDER_DATA
        else:
            folder_data_start = '/'

        fname1, _ = QFileDialog.getOpenFileName(self,
                                                "Open Excel File", folder_data_start, "Excel Files (*.xlsx)")
        fname = os.path.normpath(fname1)

        self.ui.lvLog.addItem(f"Указан файл Excel: {fname}")

        self.folder_excel_fullpath = fname
        # basename = os.path.basename(fname) # получить имя файла
        filename_without_ext = os.path.splitext(os.path.basename(fname))[0]
        self.folder_base = os.path.dirname(fname)
        file_db = os.path.join(self.folder_base, filename_without_ext + '.db')
        self.ui.lvLog.addItem(f"Установлен файл sqlite: {file_db}")
        self.db = db_sqlite
        self.db.connect()
        self.person = Person()
        # self.person.Meta.database = self.db
        self.person.create_table()
        self.person.create(name='qweqweqwe')

        # dialog = QFileDialog(self)
        # dialog.setFileMode(QFileDialog.AnyFile)
        # dialog.setNameFilter(tr("Excel files (*.xlsx)"))
        self.ui.leExcel.setText(fname)
        print(f'qeqweqweqweqweqweqwe + {fname}')


def make_gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.setGeometry(150, 150, 360, 398)
    # window.setWindowTitle("Qt Simple Example Tutorial")
    window.show()
    sys.exit(app.exec())


def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    make_gui()

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')



if __name__ == "__main__":
    main()