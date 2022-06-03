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

def make_gui():
    #root.title('Рассылка расчетных листков Квартплата24')
    # app = QtGui.QApplication(sys.argv)
    # form = QtGui.QWidget()
    # ui= Ui_frmMain()
    # ui.setupUI(form)
    # form.show()
    # sys.exit(app.exec_())

    if hasattr(Ui_frmMain,'Ui_MainWindow'):
        ui = Ui_frmMain.UiMainWindow()
    else:
        ui = Ui_frmMain.UiForm()

    app = QApplication([])
    win = QMainWindow()
    ui.setupUI(win)
    win.show()


def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    make_gui()
    # root = Root()
#    root.mainloop()

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


# import design  # Это наш конвертированный файл дизайна
#
# class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
#     def __init__(self):
#         # Это здесь нужно для доступа к переменным, методам
#         # и т.д. в файле design.py
#         super().__init__()
#         self.setupUi(self)  # Это нужно для инициализации нашего дизайна
#
# def main():
#     app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
#     window = ExampleApp()  # Создаём объект класса ExampleApp
#     window.show()  # Показываем окно
#     app.exec_()  # и запускаем приложение



if __name__ == "__main__":
    main()