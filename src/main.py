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
import json
import os
import shutil

import sys
import logging
import json

import smtplib
import ssl
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

import pendulum
from datetime import date
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QListWidgetItem)
from os import walk
import subprocess

from peewee import Table

from database import Person, Files
import pandas as pd
from dialogs import CustomDialog

from ui.main_form import Ui_frmMain
import config as cfg

def get_month_in_russian():
    today = date.today()
    month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
           'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    date_list = today.split('.')
    return (month_list[int(date_list[1]) - 1] + ' ' +
            date_list[2] + ' года')



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmMain()
        self.ui.setupUi(self)
        self.folder_excel_fullpath = ''         # полный путь к файлу Excel
        self.folder_base = ''                   # папка с Excel
        self.folder_pdf = ''                    # папка с pdf файлами
        self.ui.btnExcel.setEnabled(True)
        # убрал для дебага  - потом раскомментировать
        self.ui.btnPDF.setEnabled(False)
        self.ui.btnDoByLicID.setEnabled(False)
        self.ui.btnDoByFIO.setEnabled(False)

        self.ui.btnExcel.clicked.connect(self.open_file_excel)
        self.ui.btnPDF.clicked.connect(self.open_file_pdf)
        self.ui.btnDoByLicID.clicked.connect(self.pdf_to_folders_by_lic_id)
        self.ui.btnDoByFIO.clicked.connect(self.pdf_to_folders_by_fio)
        self.ui.btnMail.clicked.connect(self.send_mail)

        self.ui.leServer.setText(cfg.SMTP_HOST)
        self.ui.lePort.setText(cfg.SMTP_PORT)
        self.ui.leLogin.setText(cfg.SMTP_USER)
        self.ui.lePassword.setText(cfg.SMTP_PASSWORD)



        # self.ui.progressBar.setRange(0, 100)

    ''' Берем Excel файл и заноси в sqlite базу только тех, у кого есть email '''

    def excel_to_db(self):
        file_excel_full_path = self.folder_excel_fullpath
        self.folder_base = os.path.dirname(
            file_excel_full_path)  # Запомнили где лежит Excel !!
        # Создаем файлик люди_без_почты.txt
        file_users_no_email_full_path = os.path.join(
            self.folder_base, "люди_без_почты.txt")

        if os.path.isfile(file_users_no_email_full_path):
            os.remove(file_users_no_email_full_path)

        if not os.path.isfile(file_excel_full_path):
            msg_str = f"Нету файла: {file_excel_full_path}"
            logging.info(msg_str)
            # print(msg_str)
            self.ui.lvLog.addItem(msg_str)

        if os.path.isfile(file_excel_full_path):
            one_person = Person()
            one_person.create_table()
            # Load the xlsx file
            excel_data = pd.read_excel(
                file_excel_full_path,  sheet_name=cfg.EXCEL_SHEET_NAME)
            # Read the values of the fivle in the dataframe
            data = pd.DataFrame(excel_data)
            # print(data.columns)

            # print(data.count()) # выводит статистику по файлу Excel
            # msg_str = str(data.count())
            # self.ui.lvExcel.addItem(msg_str)

            cnt_load = 0
            cnt_missed = 0
            cnt_all = len(data)
            self.ui.pbMain.setRange(1, cnt_all - 1)

            print("COUNT = " + str(cnt_all))
            list_user_no_email = []
            for index, row in data.iterrows():
                tmp_str = str(row['E-mail'])
                # Выбираем всех, у кого есть почта
                if len(tmp_str) > 4:
                    cnt_load += 1
                    one_person = Person()
                    # print(row['E-mail'], row['Имя'])
                    str_adr = "д_" + \
                        str(row['Дом']) + "_" + str(row['Тип адреса Квартира']
                                                    ) + "_" + str(row['Квартира'])
                    one_person.street_addr = str_adr.replace(
                        "/", "_").replace(" ", "_")
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
                    # Вычленяем тех людей, у которых нет EMAIL
                    cnt_missed += 1
                    msg_str = str(row['Фамилия']).strip().upper(
                    ) + " " + str(row['Имя']).strip().upper() + " " + str(row['Отчество']).strip().upper()

                    # если надо с лицевым счетом
                    # + " " + str(row['Номер лицевого счета']).strip()  #
                    list_user_no_email.append(msg_str)

            # записываем всех людей без почты в файлик
            with open(file_users_no_email_full_path, 'a') as f:
                list_out = set(list_user_no_email)  # список людей без почты
                for item in list_out:
                    self.ui.lvLog.addItem(f"Нет EMAIL у:  {item} ")
                    if not item.count('\n'):
                        item = item + '\n'
                    f.write(item)
                f.close()

            # сдвигаем прогресс бар
            self.ui.pbMain.setValue(cnt_load + cnt_missed)

            self.ui.lvExcel.addItem(
                f"Найдено, что у {cnt_missed} собственников нет EMAIL")
            self.ui.lvExcel.addItem(
                f"В Базу загружено {cnt_load} собственников, у которых есть EMAIL")
            self.ui.lvLog.addItem(
                f"Найдено, что у {cnt_missed} собственников нет EMAIL")
            self.ui.lvLog.addItem(
                f"В Базу загружено {cnt_load} собственников, у которых есть EMAIL")

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

        self.excel_to_db()  # разбираем файл Excel

        self.ui.btnExcel.setEnabled(False)
        self.ui.btnPDF.setEnabled(True)

# -------------------------- начинаем работать с PDF -----------------------------------------------------------
    ''' Берем Excel файл и заноси в sqlite базу только тех, у кого есть email '''

    def pdf_to_db(self):
        folder_pdf_path = self.folder_pdf
        if not os.path.isdir(folder_pdf_path):
            msg_str = f"В папке нет файлов PDF {folder_pdf_path}"
            logging.info(msg_str)
            print(msg_str)
            self.ui.lvLog.addItem(msg_str)
        else:
            # self.ui.btnPDF.setEnabled(False);
            self.ui.tabOperations.setCurrentIndex(
                self.ui.tabOperations.currentIndex() + 1)
            filenames = []
            # r=root, d=directories, f = files
            for r, d, f in os.walk(folder_pdf_path):
                for file in f:
                    if file.endswith(".pdf") or file.endswith(".PDF"):
                        filenames.append(os.path.join(r, file))

            msg_str = f"Найдено PDF файлов: {str(len(filenames))} "
            self.ui.lvPDF.addItem(msg_str)
            self.ui.lvLog.addItem(msg_str)

            one_file = Files()
            one_file.create_table()

            for ff in filenames:
                msg_str = ff
                full_name = os.path.join(folder_pdf_path, ff)
                self.ui.lvLog.addItem(msg_str)

                filename_without_ext = str(
                    os.path.splitext(os.path.basename(ff))[0])
                adr_array = filename_without_ext.split('_')

                one_file = Files()

                one_file.file_name = full_name

                # Месяц
                one_file.month = adr_array[len(adr_array) - 1]
                adr_array.pop(len(adr_array) - 1)
                # Год
                one_file.year = "20" + adr_array[len(adr_array) - 1]
                adr_array.pop(len(adr_array) - 1)
                # Лицевой счет
                one_file.lic_id = adr_array[len(adr_array) - 1]
                adr_array.pop(len(adr_array) - 1)
                # Адрес
                str_addr = ' '.join(adr_array)
                one_file.street_addr = str_addr

                one_file.save()

    """------------- сортируем по лицевому счету -------------------------"""

    def pdf_to_folders_by_lic_id(self):
        folder_pdf_path = self.folder_pdf
        list_lic_id = []
        query = Person.select(Person.lic_id).distinct().execute()
        for li in query:
            list_lic_id.append(li.lic_id)
        # list_lic_id_sorted  = list_lic_id.sort()
        cnt_all = len(list_lic_id)
        self.ui.pbMain.setRange(1, cnt_all - 1)
        counter = 0
        for item in sorted(list_lic_id):
            counter += 1
            self.ui.pbMain.setValue(counter)
            query_person = Person.select().where(Person.lic_id == item).execute()

            if bool(query_person):
                print(item + ' ' + str(query_person.count))
                fn = item + \
                    "_" + query_person[0].surname + \
                    "_" + query_person[0].name + \
                    "_" + query_person[0].middlename + \
                    "_" + query_person[0].street_addr

                # person_json = json.dump(query_person[0])
                print(fn)
                p_fio = query_person[0].surname + "_" + \
                    query_person[0].name + "_" + query_person[0].middlename
                p_addr = query_person[0].street_addr
                p_lic_id = item
                p_email = query_person[0].email
                # формируем json
                person_json = \
                    {
                        "fio": p_fio,
                        "address": p_addr,
                        "lic_id": p_lic_id,
                        "email": p_email,
                    }

                # Запрашиваем файлы у которых есть такой лицевой счет
                query_file = Files.select().where(Files.lic_id == item).execute()
                if bool(query_person):
                    full_name_pdf_out = os.path.join(self.folder_pdf, fn)
                    print(full_name_pdf_out)

                    for fileitem in query_file:
                        str_from = fileitem.file_name
                        str_file_out_name = os.path.basename(
                            fileitem.file_name)
                        if os.path.isdir(full_name_pdf_out):
                            shutil.rmtree(full_name_pdf_out)
                        os.mkdir(full_name_pdf_out)
                        str_out = os.path.join(
                            full_name_pdf_out,  str_file_out_name)
                        str_out_json = os.path.join(
                            full_name_pdf_out, "info.json")

                        with open(str_out_json, 'w', encoding='utf-8') as f:
                            json.dump(person_json, f,
                                      ensure_ascii=False, indent=4)
                        # shutil.copy(str_from, str_out)
                        shutil.move(str_from, str_out)
                        self.ui.lvLog.addItem(
                            f"копируем из: {str_from} в: {str_out}")

            else:
                print("Файл для " + item + " - Не найден!")

        dlg = CustomDialog()
        if dlg.exec():
            self.ui.lvLog.addItem("Сортировка закончена успешно!")
            # print("Сортировка закончена успешно!")
            FILEBROWSER_PATH = os.path.join(
                os.getenv('WINDIR'), 'explorer.exe')
            if os.path.isfile(FILEBROWSER_PATH):
                subprocess.Popen(
                    [FILEBROWSER_PATH, '/select,', os.path.normpath(folder_pdf_path)])
                # subprocess.Popen(r'explorer /select, ' + folder_pdf_path)
        else:
            print("Cancel!")

        self.ui.btnPDF.setEnabled(False)
        self.ui.tabOperations.setCurrentIndex(
            self.ui.tabOperations.currentIndex() + 1)

    """------------- сортируем по ФИО -------------------------"""

    def pdf_to_folders_by_fio(self):
        folder_pdf_path = self.folder_pdf
        # list_lic_id = []

        # Запрашиваем всех и группируем по лицевому счету
        query_person = (Person
                        .select(Person.surname, Person.name, Person.middlename, Person.lic_id, Person.street_addr, Person.email)
                        .group_by(Person.lic_id)
                        .order_by(Person.lic_id)
                        .execute()
                        )

        if bool(query_person):
            for person_one in query_person:
                # print(f"сортируем по ФИО! {li.surname}")
                f1 = str(person_one.surname).strip()
                i1 = str(person_one.name).strip()
                o1 = str(person_one.middlename).strip()
                dirname = f"{f1}_{i1}_{o1}"

                dirname_full_out = os.path.join(
                    folder_pdf_path, dirname)
                print(dirname_full_out)
                if not os.path.isdir(dirname_full_out):
                    os.mkdir(dirname_full_out)

                query_files = Files.select().where(Files.lic_id == person_one.lic_id).execute()
                # print(' найдено: ' + str(query_files.count))
                if bool(query_files):
                    for file in query_files:
                        #print(person_one.surname + ' ' + str(file.file_name))
                        fn_in = file.file_name
                        shutil.move(fn_in, dirname_full_out)
                        print(fn_in)

                p_fio = str(person_one.surname) + " " +str(person_one.name) + " " +str(person_one.middlename)
                p_addr = str(person_one.street_addr)
                p_lic_id = str(person_one.lic_id)
                p_email = str(person_one.email)

                person_json = \
                    {
                        "fio": p_fio,
                        "address": p_addr,
                        "lic_id": p_lic_id,
                        "email": p_email,
                    }
                str_out_json = os.path.join(
                    dirname_full_out, "info.json")

                with open(str_out_json, 'a', encoding='utf-8') as f:
                    json.dump(person_json, f,
                              ensure_ascii=False, indent=4)

    """--------------------------------------"""
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

        # self.folder_pdf_out = os.path.join(self.folder_pdf, cfg.FOLDER_TO_MAIL)
        # self.ui.lvLog.addItem(f"Определена пака для вывода файлов PDF после сортировки: {self.folder_pdf_out}")
        #
        self.ui.lePDF.setText(self.folder_pdf)

        self.pdf_to_db()  # разбираем файл Excel
        self.ui.btnPDF.setEnabled(False)
        self.ui.btnDoByLicID.setEnabled(True)
        self.ui.btnDoByFIO.setEnabled(True)
        # self.pdf_to_folders_by_lic_id()  # сортируем по папкам по лицевому счету


    def send_mail(self):

        sender_email = self.ui.leLogin.text()
        receiver_email = self.ui.leLogin.text()
        body = 'Привет всем!!!'
        today = date.today()
        msg = MIMEMultipart()
        msg['Subject'] = 'Квитанции за месяц ' + str(today.month) + get_month_in_russian() # получаем текущую дату 'Июнь'
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # msgText = MIMEText('<b>%s</b>' % (body), 'html')
        # msg.attach(msgText)
        #
        # pdf = MIMEApplication(open("c:\\TEMP\\test.pdf", 'rb').read())
        # pdf.add_header('Content-Disposition', 'attachment', filename="test.pdf")
        # msg.attach(pdf)

        # HTML Message Part
        html = """\
        <html>
          <body>
            <p><b>Квитанции от АО «2МЕН ГРУПП»</b>
            <br>
               Пожалуйста смотрите файлы во вложении<br>
            </p>
          </body>
        </html>
        """
        part = MIMEText(html, "html")
        msg.attach(part)

        # Add Attachment
        filename = "c:\\TEMP\\test.pdf"
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        # Set mail headers
        part.add_header(
            "Content-Disposition",
            "attachment", filename=filename
        )
        msg.attach(part)

        # Add Attachment
        filename = "c:\\TEMP\\test2.pdf"
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        # Set mail headers
        part.add_header(
            "Content-Disposition",
            "attachment", filename=filename
        )
        msg.attach(part)





        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.ui.leServer.text(), self.ui.lePort.text(), context=context) as mailsender:
                #mailsender.ehlo()
                #mailsender.starttls()
                mailsender.login(self.ui.leLogin.text(), self.ui.lePassword.text())
                mailsender.sendmail(sender_email, receiver_email, msg.as_string())
                mailsender.close()

        except Exception as e:
            print(e)


def make_gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.setGeometry(150, 150, 360, 398)
    window.setWindowTitle(
        "Приложение для моей любимой Мулечки! Надеюсь поможет...")
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
