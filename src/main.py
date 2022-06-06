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
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QListWidgetItem)
from os import walk

from peewee import *
from database import Person, Files
import pandas as pd

from ui.main_form import Ui_frmMain
import config as cfg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmMain()
        self.ui.setupUi(self)
        self.folder_excel_fullpath = ''         # полный путь к файлу Excel
        self.folder_base = ''                   # папка с Excel
        self.folder_pdf = ''                    # папка с pdf файлами
        self.ui.btnExcel.setEnabled(True);
        # self.ui.btnPDF.setEnabled(False); # убрал для дебага  - потом раскомментировать

        self.ui.btnExcel.clicked.connect(self.open_file_excel)
        self.ui.btnPDF.clicked.connect(self.open_file_pdf)

        # self.ui.progressBar.setRange(0, 100)

    ''' Берем Excel файл и заноси в sqlite базу только тех, у кого есть email '''
    def excel_to_db(self):
        file_excel_full_path = self.folder_excel_fullpath
        if not os.path.isfile(file_excel_full_path):
            msg_str = f"file doesn't  exist {file_excel_full_path}"
            logging.info(msg_str)
            print(msg_str)
            self.ui.lvLog.addItem(msg_str)

        if os.path.isfile(file_excel_full_path):
            one_person = Person()
            one_person.create_table()
            # Load the xlsx file
            excel_data = pd.read_excel(file_excel_full_path,  sheet_name= cfg.EXCEL_SHEET_NAME)
            # Read the values of the file in the dataframe
            data = pd.DataFrame(excel_data)
            print(data.columns)

            # print(data.count()) # выводит статистику по файлу Excel
            # msg_str = str(data.count())
            # self.ui.lvExcel.addItem(msg_str)

            cnt_load = 0
            cnt_missed = 0
            cnt_all = len(data)
            self.ui.pbMain.setRange(1, cnt_all - 1)

            print("COUNT = " + str(cnt_all))
            for index, row in data.iterrows():
                tmp_str = str(row['E-mail'])
                # Выбираем всех, у кого есть почта
                if len(tmp_str) > 4 :
                    cnt_load += 1
                    one_person = Person()
                    # print(row['E-mail'], row['Имя'])
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

                else:
                    cnt_missed += 1
                    msg_str = str(row['Фамилия']).strip().upper()  + " " + str(row['Имя']).strip().upper() + " " +  str(row['Отчество']).strip().upper()
                    self.ui.lvLog.addItem(f"Нет EMAIL у:  {msg_str} ")

                self.ui.pbMain.setValue(cnt_load + cnt_missed) # сдвигаем прогресс бар

            self.ui.lvExcel.addItem(f"Найдено, что у {cnt_missed} пользователей нет EMAIL")
            self.ui.lvExcel.addItem(f"В Базу загружено {cnt_load} пользователей, у которых есть EMAIL")
            self.ui.lvLog.addItem(f"Найдено, что у {cnt_missed} пользователей нет EMAIL")
            self.ui.lvLog.addItem(f"В Базу загружено {cnt_load} пользователей, у которых есть EMAIL")

            # Print the content
            # print("The content of the file is:\n", data)


    ''' При нажатии на кнопку "Открыть" '''
    def open_file_excel(self):
        # self.folder_data = cfg.FOLDER_DATA
        folder_data_start = ''
        if os.path.isdir(cfg.FOLDER_DATA):
            folder_data_start = cfg.FOLDER_DATA
        else:
            folder_data_start = '/'

        if os.path.isfile(cfg.DATABASE_NAME):
            os.remove(cfg.DATABASE_NAME)


        fname1, _ = QFileDialog.getOpenFileName(self,
                                                "Open Excel File", folder_data_start, "Excel Files (*.xlsx)")
        fname = os.path.normpath(fname1)

        self.ui.lvLog.addItem(f"Указан файл Excel: {fname}")

        self.folder_excel_fullpath = fname

        # это на случай сохранения sqlite базы в папке с файликом Excel
        # filename_without_ext = os.path.splitext(os.path.basename(fname))[0]
        # self.folder_base = os.path.dirname(fname)
        # file_db = os.path.join(self.folder_base, filename_without_ext + '.db')
        # self.ui.lvLog.addItem(f"Установлен файл sqlite: {file_db}")

        self.ui.leExcel.setText(fname)

        self.excel_to_db() # разбираем файл Excel

        self.ui.btnExcel.setEnabled(False);
        self.ui.btnPDF.setEnabled(True);




    ''' Берем Excel файл и заноси в sqlite базу только тех, у кого есть email '''


    def pdf_to_db(self):
        folder_pdf_path = self.folder_pdf
        if not os.path.isdir(folder_pdf_path):
            msg_str = f"Folder with PDF files doesn't  exist {folder_pdf_path}"
            logging.info(msg_str)
            print(msg_str)
            self.ui.lvLog.addItem(msg_str)
        else:
            #self.ui.btnPDF.setEnabled(False);
            self.ui.tabOperations.setCurrentIndex(self.ui.tabOperations.currentIndex() + 1)

            filenames = next(walk(folder_pdf_path), (None, None, []))[2]  # [] if no file
            msg_str = f"Найдено PDF файлов: {str(len(filenames))} "
            self.ui.lvPDF.addItem(msg_str)
            one_file = Files()
            one_file.create_table()

            for ff in filenames:
                msg_str = ff
                self.ui.lvLog.addItem(msg_str)
                one_file = Files()
                one_file.file_name = ff
                filename_without_ext = str(os.path.splitext(os.path.basename(fname))[0])
                adr_array = filename_without_ext.split('_')

                one_file.save()






    ''' При нажатии на кнопку "Открыть" и указываем файл PDF'''
    def open_file_pdf(self):
        if os.path.isdir(cfg.FOLDER_DATA):
            folder_data_start = cfg.FOLDER_DATA
        else:
            folder_data_start = '/'

        fname1, _ = QFileDialog.getOpenFileName(self,
                                                "Open PDF File", folder_data_start, "PDF Files (*.pdf)")
        fname = os.path.normpath(fname1)
        self.ui.pbMain.setValue(0)  # сдвигаем прогресс бар

        self.ui.lvLog.addItem(f"Указан файл PDF: {fname}")

        self.folder_pdf = os.path.dirname(fname)
        self.ui.lePDF.setText(self.folder_pdf)

        self.pdf_to_db() # разбираем файл Excel


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