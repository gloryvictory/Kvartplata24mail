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
from PySide6.QtWidgets import QApplication, QMainWindow

# from PySide6 import QtUiTools
# from PySide6.QtGui import *

from PySide6.QtWidgets import (QApplication, QMainWindow)

# from PySide6.QtCore import (QCoreApplication, QtGui, QDate, QDateTime, QLocale,
#     QMetaObject, QObject, QPoint, QRect,
#     QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
# from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QListWidget,
#     QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
#     QSizePolicy, QStatusBar, QTabWidget, QWidget)

from ui.main_form import Ui_frmMain

from core.logger import get_logger
import config

logger = get_logger()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frmMain()
        self.ui.setupUi(self)

        self.ui.btnExcel.clicked.connect(self.test)
    def test(self):
        print('qeqweqweqweqweqweqwe')

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