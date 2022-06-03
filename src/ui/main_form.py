# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QWidget)

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        if not frmMain.objectName():
            frmMain.setObjectName(u"frmMain")
        frmMain.resize(1110, 804)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmMain.sizePolicy().hasHeightForWidth())
        frmMain.setSizePolicy(sizePolicy)
        frmMain.setMinimumSize(QSize(1110, 804))
        frmMain.setMaximumSize(QSize(1110, 804))
        self.centralwidget = QWidget(frmMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 1091, 51))
        self.leExcel = QLineEdit(self.groupBox)
        self.leExcel.setObjectName(u"leExcel")
        self.leExcel.setGeometry(QRect(10, 20, 991, 22))
        self.leExcel.setReadOnly(True)
        self.btnExcel = QPushButton(self.groupBox)
        self.btnExcel.setObjectName(u"btnExcel")
        self.btnExcel.setGeometry(QRect(1010, 20, 75, 24))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 50, 1091, 51))
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 20, 991, 22))
        self.lineEdit_2.setReadOnly(True)
        self.btnExcel_2 = QPushButton(self.groupBox_2)
        self.btnExcel_2.setObjectName(u"btnExcel_2")
        self.btnExcel_2.setGeometry(QRect(1010, 20, 75, 24))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 110, 1091, 651))
        self.tabOperations = QTabWidget(self.groupBox_3)
        self.tabOperations.setObjectName(u"tabOperations")
        self.tabOperations.setGeometry(QRect(0, 20, 1091, 621))
        self.tabOperations.setMovable(True)
        self.tabExcel = QWidget()
        self.tabExcel.setObjectName(u"tabExcel")
        self.tabOperations.addTab(self.tabExcel, "")
        self.tabPDF = QWidget()
        self.tabPDF.setObjectName(u"tabPDF")
        self.tabOperations.addTab(self.tabPDF, "")
        self.tabLog = QWidget()
        self.tabLog.setObjectName(u"tabLog")
        self.listWidget = QListWidget(self.tabLog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 1091, 601))
        self.tabOperations.addTab(self.tabLog, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabOperations.addTab(self.tab, "")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 760, 1101, 23))
        self.progressBar.setValue(1)
        frmMain.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frmMain)
        self.statusbar.setObjectName(u"statusbar")
        frmMain.setStatusBar(self.statusbar)

        self.retranslateUi(frmMain)

        self.tabOperations.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frmMain)
    # setupUi

    def retranslateUi(self, frmMain):
        frmMain.setWindowTitle(QCoreApplication.translate("frmMain", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("frmMain", u"\u0424\u0430\u0439\u043b Excel", None))
        self.leExcel.setInputMask("")
        self.leExcel.setText(QCoreApplication.translate("frmMain", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \"\u041e\u0442\u043a\u0440\u044b\u0442\u044c\" \u0438 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0433\u0434\u0435 \u043b\u0435\u0436\u0438\u0442 \"Excel\" \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.btnExcel.setText(QCoreApplication.translate("frmMain", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("frmMain", u"\u041f\u0430\u043f\u043a\u0430 \u0441 PDF \u0444\u0430\u0439\u043b\u0430\u043c\u0438:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("frmMain", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \"\u041e\u0442\u043a\u0440\u044b\u0442\u044c\" \u0438 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0433\u0434\u0435 \u043b\u0435\u0436\u0430\u0442 \u0444\u0430\u0439\u043b\u044b pdf", None))
        self.btnExcel_2.setText(QCoreApplication.translate("frmMain", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("frmMain", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.tabOperations.setTabText(self.tabOperations.indexOf(self.tabExcel), QCoreApplication.translate("frmMain", u"Excel", None))
        self.tabOperations.setTabText(self.tabOperations.indexOf(self.tabPDF), QCoreApplication.translate("frmMain", u"PDF", None))
        self.tabOperations.setTabText(self.tabOperations.indexOf(self.tabLog), QCoreApplication.translate("frmMain", u"\u0416\u0443\u0440\u043d\u0430\u043b", None))
        self.tabOperations.setTabText(self.tabOperations.indexOf(self.tab), QCoreApplication.translate("frmMain", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

