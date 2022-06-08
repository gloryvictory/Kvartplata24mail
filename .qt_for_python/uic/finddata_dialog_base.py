# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finddata_dialog_base.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_finddataDialogBase(object):
    def setupUi(self, finddataDialogBase):
        if not finddataDialogBase.objectName():
            finddataDialogBase.setObjectName(u"finddataDialogBase")
        finddataDialogBase.resize(469, 452)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(finddataDialogBase.sizePolicy().hasHeightForWidth())
        finddataDialogBase.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        finddataDialogBase.setWindowIcon(icon)
        finddataDialogBase.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        finddataDialogBase.setSizeGripEnabled(True)
        finddataDialogBase.setModal(True)
        self.gridLayout_2 = QGridLayout(finddataDialogBase)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(finddataDialogBase)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabLog = QWidget()
        self.tabLog.setObjectName(u"tabLog")
        self.gridLayout_3 = QGridLayout(self.tabLog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lvLog = QListWidget(self.tabLog)
        self.lvLog.setObjectName(u"lvLog")
        sizePolicy.setHeightForWidth(self.lvLog.sizePolicy().hasHeightForWidth())
        self.lvLog.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.lvLog, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabLog, "")
        self.tabVector = QWidget()
        self.tabVector.setObjectName(u"tabVector")
        self.gridLayout_4 = QGridLayout(self.tabVector)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget = QTableWidget(self.tabVector)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(10)

        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabVector, "")
        self.tabStat = QWidget()
        self.tabStat.setObjectName(u"tabStat")
        self.gridLayout_5 = QGridLayout(self.tabStat)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget.addTab(self.tabStat, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnApply = QPushButton(finddataDialogBase)
        self.btnApply.setObjectName(u"btnApply")

        self.horizontalLayout.addWidget(self.btnApply)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 3, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.edtFolder = QLineEdit(finddataDialogBase)
        self.edtFolder.setObjectName(u"edtFolder")

        self.gridLayout.addWidget(self.edtFolder, 0, 1, 1, 1)

        self.btnSelectFolder = QToolButton(finddataDialogBase)
        self.btnSelectFolder.setObjectName(u"btnSelectFolder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnSelectFolder.sizePolicy().hasHeightForWidth())
        self.btnSelectFolder.setSizePolicy(sizePolicy1)
        self.btnSelectFolder.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.btnSelectFolder, 0, 3, 1, 1)

        self.label = QLabel(finddataDialogBase)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.line = QFrame(finddataDialogBase)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 2)


        self.retranslateUi(finddataDialogBase)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(finddataDialogBase)
    # setupUi

    def retranslateUi(self, finddataDialogBase):
        finddataDialogBase.setWindowTitle(QCoreApplication.translate("finddataDialogBase", u"finddata", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLog), QCoreApplication.translate("finddataDialogBase", u"Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVector), QCoreApplication.translate("finddataDialogBase", u"Vector", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStat), QCoreApplication.translate("finddataDialogBase", u"Statistics", None))
        self.btnApply.setText(QCoreApplication.translate("finddataDialogBase", u"Apply", None))
#if QT_CONFIG(tooltip)
        self.edtFolder.setToolTip(QCoreApplication.translate("finddataDialogBase", u"Please scpecify folder or disk", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnSelectFolder.setStatusTip(QCoreApplication.translate("finddataDialogBase", u"Please Select Root Folder for scaning", None))
#endif // QT_CONFIG(statustip)
        self.btnSelectFolder.setText(QCoreApplication.translate("finddataDialogBase", u"...", None))
        self.label.setText(QCoreApplication.translate("finddataDialogBase", u"<html><head/><body><p>Folder</p></body></html>", None))
    # retranslateUi

