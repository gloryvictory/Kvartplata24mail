# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui_2.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

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
        self.lePDF = QLineEdit(self.groupBox_2)
        self.lePDF.setObjectName(u"lePDF")
        self.lePDF.setGeometry(QRect(10, 20, 991, 22))
        self.lePDF.setReadOnly(True)
        self.btnPDF = QPushButton(self.groupBox_2)
        self.btnPDF.setObjectName(u"btnPDF")
        self.btnPDF.setGeometry(QRect(1010, 20, 75, 24))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 110, 1091, 651))
        self.tabOperations = QTabWidget(self.groupBox_3)
        self.tabOperations.setObjectName(u"tabOperations")
        self.tabOperations.setGeometry(QRect(0, 20, 1091, 631))
        self.tabOperations.setMovable(True)
        self.tabExcel = QWidget()
        self.tabExcel.setObjectName(u"tabExcel")
        self.lvExcel = QListWidget(self.tabExcel)
        self.lvExcel.setObjectName(u"lvExcel")
        self.lvExcel.setGeometry(QRect(0, 0, 1091, 611))
        self.tabOperations.addTab(self.tabExcel, "")
        self.tabPDF = QWidget()
        self.tabPDF.setObjectName(u"tabPDF")
        self.lvPDF = QListWidget(self.tabPDF)
        self.lvPDF.setObjectName(u"lvPDF")
        self.lvPDF.setGeometry(QRect(0, 0, 1091, 611))
        self.tabOperations.addTab(self.tabPDF, "")
        self.tabMail = QWidget()
        self.tabMail.setObjectName(u"tabMail")
        self.gbServer = QGroupBox(self.tabMail)
        self.gbServer.setObjectName(u"gbServer")
        self.gbServer.setGeometry(QRect(10, 10, 401, 80))
        self.lblServer = QLabel(self.gbServer)
        self.lblServer.setObjectName(u"lblServer")
        self.lblServer.setGeometry(QRect(10, 20, 49, 16))
        self.lblPort = QLabel(self.gbServer)
        self.lblPort.setObjectName(u"lblPort")
        self.lblPort.setGeometry(QRect(10, 50, 49, 16))
        self.leServer = QLineEdit(self.gbServer)
        self.leServer.setObjectName(u"leServer")
        self.leServer.setGeometry(QRect(50, 20, 341, 22))
        self.lePort = QLineEdit(self.gbServer)
        self.lePort.setObjectName(u"lePort")
        self.lePort.setGeometry(QRect(50, 50, 341, 22))
        self.groupBox_4 = QGroupBox(self.tabMail)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(430, 10, 381, 80))
        self.lblLogin = QLabel(self.groupBox_4)
        self.lblLogin.setObjectName(u"lblLogin")
        self.lblLogin.setGeometry(QRect(10, 20, 49, 16))
        self.leLogin = QLineEdit(self.groupBox_4)
        self.leLogin.setObjectName(u"leLogin")
        self.leLogin.setGeometry(QRect(70, 20, 301, 22))
        self.lblPassword = QLabel(self.groupBox_4)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setGeometry(QRect(10, 50, 61, 16))
        self.lePassword = QLineEdit(self.groupBox_4)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setGeometry(QRect(70, 50, 301, 22))
        self.btnMail = QPushButton(self.tabMail)
        self.btnMail.setObjectName(u"btnMail")
        self.btnMail.setGeometry(QRect(830, 20, 241, 71))
        self.groupBox_5 = QGroupBox(self.tabMail)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 90, 1061, 51))
        self.lineEdit = QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 1041, 22))
        self.groupBox_6 = QGroupBox(self.tabMail)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 140, 1061, 461))
        self.lvLogMail = QListWidget(self.groupBox_6)
        self.lvLogMail.setObjectName(u"lvLogMail")
        self.lvLogMail.setGeometry(QRect(0, 20, 1051, 431))
        self.tabOperations.addTab(self.tabMail, "")
        self.tabLog = QWidget()
        self.tabLog.setObjectName(u"tabLog")
        self.lvLog = QListWidget(self.tabLog)
        self.lvLog.setObjectName(u"lvLog")
        self.lvLog.setGeometry(QRect(0, 0, 1091, 611))
        self.tabOperations.addTab(self.tabLog, "")
        self.pbMain = QProgressBar(self.centralwidget)
        self.pbMain.setObjectName(u"pbMain")
        self.pbMain.setGeometry(QRect(10, 760, 1101, 23))
        self.pbMain.setValue(0)
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
        self.lePDF.setText(QCoreApplication.translate("frmMain", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \"\u041e\u0442\u043a\u0440\u044b\u0442\u044c\" \u0438 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0433\u0434\u0435 \u043b\u0435\u0436\u0430\u0442 \u0444\u0430\u0439\u043b\u044b pdf", None))
        self.btnPDF.setText(QCoreApplication.translate("frmMain", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("frmMain", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.tabOperations.setTabText(self.tabOperations.indexOf(self.tabExcel), QCoreApplication.translate("frmMain", u"Excel", None))
        self.tabOperations.setTabText(self.tabOperations.indexOf(self.tabPDF), QCoreApplication.translate("frmMain", u"PDF", None))
        self.gbServer.setTitle(QCoreApplication.translate("frmMain", u"\u0421\u0435\u0440\u0432\u0435\u0440 SMTP:", None))
        self.lblServer.setText(QCoreApplication.translate("frmMain", u"Server:", None))
        self.lblPort.setText(QCoreApplication.translate("frmMain", u"Port:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("frmMain", u"User:", None))
        self.lblLogin.setText(QCoreApplication.translate("frmMain", u"Login:", None))
        self.lblPassword.setText(QCoreApplication.translate("frmMain", u"Password:", None))
        self.btnMail.setText(QCoreApplication.translate("frmMain", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("frmMain", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("frmMain", u"\u0416\u0443\u0440\u043d\u0430\u043b:", None))
        self.tabOperations.setTabText(self.tabOperations.indexOf(self.tabMail), QCoreApplication.translate("frmMain", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u043e\u0447\u0442\u044b", None))
        self.tabOperations.setTabText(self.tabOperations.indexOf(self.tabLog), QCoreApplication.translate("frmMain", u"\u0416\u0443\u0440\u043d\u0430\u043b", None))
    # retranslateUi

