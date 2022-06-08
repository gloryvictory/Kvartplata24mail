# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form_1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        if not frmMain.objectName():
            frmMain.setObjectName(u"frmMain")
        frmMain.resize(750, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmMain.sizePolicy().hasHeightForWidth())
        frmMain.setSizePolicy(sizePolicy)
        frmMain.setMinimumSize(QSize(750, 550))
        self.centralwidget = QWidget(frmMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.leExcel = QLineEdit(self.groupBox)
        self.leExcel.setObjectName(u"leExcel")
        self.leExcel.setReadOnly(True)

        self.gridLayout_2.addWidget(self.leExcel, 0, 0, 1, 1)

        self.btnExcel = QPushButton(self.groupBox)
        self.btnExcel.setObjectName(u"btnExcel")

        self.gridLayout_2.addWidget(self.btnExcel, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lePDF = QLineEdit(self.groupBox_2)
        self.lePDF.setObjectName(u"lePDF")
        self.lePDF.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lePDF, 0, 0, 1, 1)

        self.btnPDF = QPushButton(self.groupBox_2)
        self.btnPDF.setObjectName(u"btnPDF")

        self.gridLayout_3.addWidget(self.btnPDF, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabOperations = QTabWidget(self.groupBox_3)
        self.tabOperations.setObjectName(u"tabOperations")
        self.tabOperations.setMovable(True)
        self.tabExcel = QWidget()
        self.tabExcel.setObjectName(u"tabExcel")
        self.gridLayout_5 = QGridLayout(self.tabExcel)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lvExcel = QListWidget(self.tabExcel)
        self.lvExcel.setObjectName(u"lvExcel")

        self.gridLayout_5.addWidget(self.lvExcel, 0, 0, 1, 1)

        self.tabOperations.addTab(self.tabExcel, "")
        self.tabPDF = QWidget()
        self.tabPDF.setObjectName(u"tabPDF")
        self.gridLayout_6 = QGridLayout(self.tabPDF)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lvPDF = QListWidget(self.tabPDF)
        self.lvPDF.setObjectName(u"lvPDF")

        self.gridLayout_6.addWidget(self.lvPDF, 0, 0, 1, 1)

        self.tabOperations.addTab(self.tabPDF, "")
        self.tabMail = QWidget()
        self.tabMail.setObjectName(u"tabMail")
        self.gridLayout_9 = QGridLayout(self.tabMail)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.btnMail = QPushButton(self.tabMail)
        self.btnMail.setObjectName(u"btnMail")

        self.gridLayout_8.addWidget(self.btnMail, 5, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.tabMail)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.leLogin = QLineEdit(self.groupBox_4)
        self.leLogin.setObjectName(u"leLogin")

        self.gridLayout_10.addWidget(self.leLogin, 1, 0, 1, 1)

        self.lblLogin = QLabel(self.groupBox_4)
        self.lblLogin.setObjectName(u"lblLogin")

        self.gridLayout_10.addWidget(self.lblLogin, 0, 0, 1, 1)

        self.lblPassword = QLabel(self.groupBox_4)
        self.lblPassword.setObjectName(u"lblPassword")

        self.gridLayout_10.addWidget(self.lblPassword, 2, 0, 1, 1)

        self.lePassword = QLineEdit(self.groupBox_4)
        self.lePassword.setObjectName(u"lePassword")

        self.gridLayout_10.addWidget(self.lePassword, 3, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.gbServer = QGroupBox(self.tabMail)
        self.gbServer.setObjectName(u"gbServer")
        self.gridLayout_11 = QGridLayout(self.gbServer)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.lePort = QLineEdit(self.gbServer)
        self.lePort.setObjectName(u"lePort")

        self.gridLayout_11.addWidget(self.lePort, 3, 1, 1, 1)

        self.lblPort = QLabel(self.gbServer)
        self.lblPort.setObjectName(u"lblPort")

        self.gridLayout_11.addWidget(self.lblPort, 2, 1, 1, 1)

        self.leServer = QLineEdit(self.gbServer)
        self.leServer.setObjectName(u"leServer")

        self.gridLayout_11.addWidget(self.leServer, 1, 1, 1, 1)

        self.lblServer = QLabel(self.gbServer)
        self.lblServer.setObjectName(u"lblServer")

        self.gridLayout_11.addWidget(self.lblServer, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.gbServer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 6, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.tabOperations.addTab(self.tabMail, "")
        self.tabLog = QWidget()
        self.tabLog.setObjectName(u"tabLog")
        self.gridLayout_7 = QGridLayout(self.tabLog)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lvLog = QListWidget(self.tabLog)
        self.lvLog.setObjectName(u"lvLog")

        self.gridLayout_7.addWidget(self.lvLog, 0, 0, 1, 1)

        self.tabOperations.addTab(self.tabLog, "")

        self.gridLayout_4.addWidget(self.tabOperations, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.pbMain = QProgressBar(self.centralwidget)
        self.pbMain.setObjectName(u"pbMain")
        self.pbMain.setValue(0)

        self.verticalLayout_2.addWidget(self.pbMain)

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
        self.btnMail.setText(QCoreApplication.translate("frmMain", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("frmMain", u"User:", None))
        self.lblLogin.setText(QCoreApplication.translate("frmMain", u"Login:", None))
        self.lblPassword.setText(QCoreApplication.translate("frmMain", u"Password:", None))
        self.gbServer.setTitle(QCoreApplication.translate("frmMain", u"\u0421\u0435\u0440\u0432\u0435\u0440 SMTP:", None))
        self.lblPort.setText(QCoreApplication.translate("frmMain", u"Port:", None))
        self.lblServer.setText(QCoreApplication.translate("frmMain", u"Server:", None))
        self.tabOperations.setTabText(self.tabOperations.indexOf(self.tabMail), QCoreApplication.translate("frmMain", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u043e\u0447\u0442\u044b", None))
        self.tabOperations.setTabText(self.tabOperations.indexOf(self.tabLog), QCoreApplication.translate("frmMain", u"\u0416\u0443\u0440\u043d\u0430\u043b", None))
    # retranslateUi

