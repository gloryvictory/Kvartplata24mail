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
from datetime import datetime
# from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog)



from ui.main_form import Ui_frmMain

from core.logger import get_logger
import config as cfg

logger = get_logger()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmMain()
        self.ui.setupUi(self)
        self.folder_excel_fullpath = '' # полный путь к файлу Excel


        self.ui.btnExcel.clicked.connect(self.OpenFileExcel)
    def OpenFileExcel(self):
        # self.folder_data = cfg.FOLDER_DATA
        folder_data_start = ''
        if os.path.isdir(cfg.FOLDER_DATA):
            folder_data_start = cfg.FOLDER_DATA

        else:
            folder_data_start = '/'

        fname, _  = QFileDialog.getOpenFileName(self,
                                                "Open Excel File", folder_data_start, "Excel Files (*.xlsx)")
        fname = os.path.normpath(fname)
        self.folder_excel_fullpath = fname
        print(os.path.dirname(fname))
        basename = os.path.basename(fname)
        print(basename)
        basename_without_ext = os.path.splitext(os.path.basename(fname))[0]
        print(basename_without_ext)
        path_db = os.path.join(os.path.dirname(fname), basename_without_ext + '.db')
        print(path_db)

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