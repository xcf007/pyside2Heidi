# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from .database_table_info import DatabaseTableInfo

from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1218, 849)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setBaseSize(QSize(200, 0))
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/heidi.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionSession_Manager = QAction(MainWindow)
        self.actionSession_Manager.setObjectName(u"actionSession_Manager")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/arrow_refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRefresh.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.databaseTree = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.databaseTree.setHeaderItem(__qtreewidgetitem)
        self.databaseTree.setObjectName(u"databaseTree")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.databaseTree.sizePolicy().hasHeightForWidth())
        self.databaseTree.setSizePolicy(sizePolicy1)
        self.databaseTree.setMaximumSize(QSize(16777215, 16777215))
        self.databaseTree.setBaseSize(QSize(350, 0))
        self.databaseTree.setLayoutDirection(Qt.LeftToRight)
        self.databaseTree.setRootIsDecorated(False)
        self.databaseTree.setUniformRowHeights(True)
        self.databaseTree.setHeaderHidden(True)
        self.databaseTree.setColumnCount(1)
        self.splitter.addWidget(self.databaseTree)
        self.twMachineTabs = QTabWidget(self.splitter)
        self.twMachineTabs.setObjectName(u"twMachineTabs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.twMachineTabs.sizePolicy().hasHeightForWidth())
        self.twMachineTabs.setSizePolicy(sizePolicy2)
        self.twMachineTabs.setTabShape(QTabWidget.Rounded)
        self.machineTab = QWidget()
        self.machineTab.setObjectName(u"machineTab")
        self.verticalLayout_3 = QVBoxLayout(self.machineTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.processListTab = QTabWidget(self.machineTab)
        self.processListTab.setObjectName(u"processListTab")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.processListTree = QTreeWidget(self.tab)
        self.processListTree.setObjectName(u"processListTree")
        self.processListTree.setSortingEnabled(True)

        self.verticalLayout_4.addWidget(self.processListTree)

        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/resultset_next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.processListTab.addTab(self.tab, icon2, "")
        self.hostTabDB = QWidget()
        self.hostTabDB.setObjectName(u"hostTabDB")
        self.verticalLayout_2 = QVBoxLayout(self.hostTabDB)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.hostTabDB)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/icons/database.png", QSize(), QIcon.Normal, QIcon.On)
        self.processListTab.addTab(self.hostTabDB, icon3, "")

        self.verticalLayout_3.addWidget(self.processListTab)

        icon4 = QIcon()
        icon4.addFile(u":/icons/resources/icons/computer.png", QSize(), QIcon.Normal, QIcon.On)
        self.twMachineTabs.addTab(self.machineTab, icon4, "")
        self.databaseTab = QWidget()
        self.databaseTab.setObjectName(u"databaseTab")
        self.horizontalLayout = QHBoxLayout(self.databaseTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.databaseInfoTable = QTableWidget(self.databaseTab)
        if (self.databaseInfoTable.columnCount() < 8):
            self.databaseInfoTable.setColumnCount(8)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.databaseInfoTable.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.databaseInfoTable.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.databaseInfoTable.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.databaseInfoTable.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.databaseInfoTable.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.databaseInfoTable.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.databaseInfoTable.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.databaseInfoTable.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        self.databaseInfoTable.setObjectName(u"databaseInfoTable")
        self.databaseInfoTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.databaseInfoTable.setAlternatingRowColors(False)
        self.databaseInfoTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.databaseInfoTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.databaseInfoTable.setSortingEnabled(True)
        self.databaseInfoTable.setCornerButtonEnabled(False)
        self.databaseInfoTable.horizontalHeader().setMinimumSectionSize(50)
        self.databaseInfoTable.horizontalHeader().setDefaultSectionSize(80)
        self.databaseInfoTable.horizontalHeader().setHighlightSections(False)
        self.databaseInfoTable.horizontalHeader().setStretchLastSection(True)
        self.databaseInfoTable.verticalHeader().setVisible(False)
        self.databaseInfoTable.verticalHeader().setMinimumSectionSize(15)
        self.databaseInfoTable.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout.addWidget(self.databaseInfoTable)

        icon5 = QIcon()
        icon5.addFile(u":/icons/resources/icons/database.png", QSize(), QIcon.Normal, QIcon.Off)
        self.twMachineTabs.addTab(self.databaseTab, icon5, "")
        self.tableTab = QWidget()
        self.tableTab.setObjectName(u"tableTab")
        self.horizontalLayout_4 = QHBoxLayout(self.tableTab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.splitter_3 = QSplitter(self.tableTab)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.tableTabs = QTabWidget(self.splitter_3)
        self.tableTabs.setObjectName(u"tableTabs")
        self.tableTabs.setStyleSheet(u"QPushButton {\n"
"	padding: 0px;\n"
"	text-align: left;\n"
"}")
        self.tableTabsBasic = QWidget()
        self.tableTabsBasic.setObjectName(u"tableTabsBasic")
        self.horizontalLayout_5 = QHBoxLayout(self.tableTabsBasic)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.tableTabsBasic)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.tableName = QLineEdit(self.tableTabsBasic)
        self.tableName.setObjectName(u"tableName")

        self.gridLayout_3.addWidget(self.tableName, 0, 1, 1, 1)

        self.label_3 = QLabel(self.tableTabsBasic)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.tableComment = QPlainTextEdit(self.tableTabsBasic)
        self.tableComment.setObjectName(u"tableComment")

        self.gridLayout_3.addWidget(self.tableComment, 1, 1, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_3)

        icon6 = QIcon()
        icon6.addFile(u":/icons/resources/icons/table.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tableTabs.addTab(self.tableTabsBasic, icon6, "")
        self.tableTabsOptions = QWidget()
        self.tableTabsOptions.setObjectName(u"tableTabsOptions")
        self.verticalLayout_6 = QVBoxLayout(self.tableTabsOptions)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.tableTabsOptions)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.tableOptionsAutoIncrement = QLineEdit(self.tableTabsOptions)
        self.tableOptionsAutoIncrement.setObjectName(u"tableOptionsAutoIncrement")

        self.gridLayout.addWidget(self.tableOptionsAutoIncrement, 0, 1, 1, 1)

        self.label_5 = QLabel(self.tableTabsOptions)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.tableOptionsDefaultCollation = QComboBox(self.tableTabsOptions)
        self.tableOptionsDefaultCollation.setObjectName(u"tableOptionsDefaultCollation")

        self.gridLayout.addWidget(self.tableOptionsDefaultCollation, 0, 3, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.verticalLayout_6.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        icon7 = QIcon()
        icon7.addFile(u":/icons/resources/icons/wrench.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tableTabs.addTab(self.tableTabsOptions, icon7, "")
        self.tableTabsIndexes = QWidget()
        self.tableTabsIndexes.setObjectName(u"tableTabsIndexes")
        self.horizontalLayout_3 = QHBoxLayout(self.tableTabsIndexes)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.addColumnButton_2 = QPushButton(self.tableTabsIndexes)
        self.addColumnButton_2.setObjectName(u"addColumnButton_2")
        self.addColumnButton_2.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/resources/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addColumnButton_2.setIcon(icon8)
        self.addColumnButton_2.setFlat(True)

        self.verticalLayout_7.addWidget(self.addColumnButton_2)

        self.removeColumnButton_2 = QPushButton(self.tableTabsIndexes)
        self.removeColumnButton_2.setObjectName(u"removeColumnButton_2")
        self.removeColumnButton_2.setEnabled(False)
        icon9 = QIcon()
        icon9.addFile(u":/icons/resources/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removeColumnButton_2.setIcon(icon9)
        self.removeColumnButton_2.setFlat(True)

        self.verticalLayout_7.addWidget(self.removeColumnButton_2)

        self.pushButton = QPushButton(self.tableTabsIndexes)
        self.pushButton.setObjectName(u"pushButton")
        icon10 = QIcon()
        icon10.addFile(u":/icons/resources/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon10)
        self.pushButton.setFlat(True)

        self.verticalLayout_7.addWidget(self.pushButton)

        self.moveColumnUpButton_2 = QPushButton(self.tableTabsIndexes)
        self.moveColumnUpButton_2.setObjectName(u"moveColumnUpButton_2")
        self.moveColumnUpButton_2.setEnabled(False)
        icon11 = QIcon()
        icon11.addFile(u":/icons/resources/icons/resultset_up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.moveColumnUpButton_2.setIcon(icon11)
        self.moveColumnUpButton_2.setFlat(True)

        self.verticalLayout_7.addWidget(self.moveColumnUpButton_2)

        self.moveColumnDownButton_2 = QPushButton(self.tableTabsIndexes)
        self.moveColumnDownButton_2.setObjectName(u"moveColumnDownButton_2")
        self.moveColumnDownButton_2.setEnabled(False)
        icon12 = QIcon()
        icon12.addFile(u":/icons/resources/icons/resultset_down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.moveColumnDownButton_2.setIcon(icon12)
        self.moveColumnDownButton_2.setFlat(True)

        self.verticalLayout_7.addWidget(self.moveColumnDownButton_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.indexes = QTreeWidget(self.tableTabsIndexes)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"Name");
        self.indexes.setHeaderItem(__qtreewidgetitem1)
        self.indexes.setObjectName(u"indexes")

        self.horizontalLayout_3.addWidget(self.indexes)

        icon13 = QIcon()
        icon13.addFile(u":/icons/resources/icons/lightning.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tableTabs.addTab(self.tableTabsIndexes, icon13, "")
        self.createCode = QWidget()
        self.createCode.setObjectName(u"createCode")
        self.horizontalLayout_6 = QHBoxLayout(self.createCode)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.txtCreateCode = QPlainTextEdit(self.createCode)
        self.txtCreateCode.setObjectName(u"txtCreateCode")
        self.txtCreateCode.setTabStopWidth(20)

        self.horizontalLayout_6.addWidget(self.txtCreateCode)

        icon14 = QIcon()
        icon14.addFile(u":/icons/resources/icons/page_white_gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tableTabs.addTab(self.createCode, icon14, "")
        self.splitter_3.addWidget(self.tableTabs)
        self.layoutWidget = QWidget(self.splitter_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self._2 = QHBoxLayout()
        self._2.setObjectName(u"_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self._2.addWidget(self.label)

        self.addColumnButton = QPushButton(self.layoutWidget)
        self.addColumnButton.setObjectName(u"addColumnButton")
        self.addColumnButton.setIcon(icon8)
        self.addColumnButton.setFlat(True)

        self._2.addWidget(self.addColumnButton)

        self.removeColumnButton = QPushButton(self.layoutWidget)
        self.removeColumnButton.setObjectName(u"removeColumnButton")
        self.removeColumnButton.setEnabled(False)
        self.removeColumnButton.setIcon(icon9)
        self.removeColumnButton.setFlat(True)

        self._2.addWidget(self.removeColumnButton)

        self.moveColumnUpButton = QPushButton(self.layoutWidget)
        self.moveColumnUpButton.setObjectName(u"moveColumnUpButton")
        self.moveColumnUpButton.setEnabled(False)
        self.moveColumnUpButton.setIcon(icon11)
        self.moveColumnUpButton.setFlat(True)

        self._2.addWidget(self.moveColumnUpButton)

        self.moveColumnDownButton = QPushButton(self.layoutWidget)
        self.moveColumnDownButton.setObjectName(u"moveColumnDownButton")
        self.moveColumnDownButton.setEnabled(False)
        self.moveColumnDownButton.setIcon(icon12)
        self.moveColumnDownButton.setFlat(True)

        self._2.addWidget(self.moveColumnDownButton)

        self.horizontalSpacer = QSpacerItem(13, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addLayout(self._2)

        self.tableInfoTable = DatabaseTableInfo(self.layoutWidget)
        if (self.tableInfoTable.columnCount() < 12):
            self.tableInfoTable.setColumnCount(12)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(8, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(9, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(10, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableInfoTable.setHorizontalHeaderItem(11, __qtablewidgetitem30)
        self.tableInfoTable.setObjectName(u"tableInfoTable")
        self.tableInfoTable.setStyleSheet(u"QTableWidget::item {\n"
"	padding: 0px;\n"
"}")
        self.tableInfoTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableInfoTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableInfoTable.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.tableInfoTable)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.discardTableButton = QPushButton(self.layoutWidget)
        self.discardTableButton.setObjectName(u"discardTableButton")
        self.discardTableButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.discardTableButton)

        self.saveTableButton = QPushButton(self.layoutWidget)
        self.saveTableButton.setObjectName(u"saveTableButton")
        self.saveTableButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.saveTableButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.splitter_3.addWidget(self.layoutWidget)

        self.horizontalLayout_4.addWidget(self.splitter_3)

        self.twMachineTabs.addTab(self.tableTab, icon6, "")
        self.splitter.addWidget(self.twMachineTabs)
        self.splitter_2.addWidget(self.splitter)
        self.txtStatus = QTextEdit(self.splitter_2)
        self.txtStatus.setObjectName(u"txtStatus")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txtStatus.sizePolicy().hasHeightForWidth())
        self.txtStatus.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txtStatus.setFont(font)
        self.txtStatus.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.splitter_2.addWidget(self.txtStatus)

        self.verticalLayout.addWidget(self.splitter_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1218, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSession_Manager)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.toolBar.addAction(self.actionRefresh)

        self.retranslateUi(MainWindow)

        self.twMachineTabs.setCurrentIndex(2)
        self.processListTab.setCurrentIndex(0)
        self.tableTabs.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"pyHeidi", None))
        self.actionSession_Manager.setText(QCoreApplication.translate("MainWindow", u"Session Manager", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        ___qtreewidgetitem = self.processListTree.headerItem()
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Info", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"State", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Command", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"DB", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Host", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"User", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"id", None));
        self.processListTab.setTabText(self.processListTab.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Processes", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Database", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Items", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Last Modification", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Tables", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Views", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Functions", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Procedures", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Triggers", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Events", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Default Collation", None));
        self.processListTab.setTabText(self.processListTab.indexOf(self.hostTabDB), QCoreApplication.translate("MainWindow", u"Databases (0)", None))
        self.twMachineTabs.setTabText(self.twMachineTabs.indexOf(self.machineTab), QCoreApplication.translate("MainWindow", u"Host: ", None))
        ___qtablewidgetitem11 = self.databaseInfoTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem12 = self.databaseInfoTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Rows", None));
        ___qtablewidgetitem13 = self.databaseInfoTable.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtablewidgetitem14 = self.databaseInfoTable.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Created", None));
        ___qtablewidgetitem15 = self.databaseInfoTable.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Updated", None));
        ___qtablewidgetitem16 = self.databaseInfoTable.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Engine", None));
        ___qtablewidgetitem17 = self.databaseInfoTable.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Comment", None));
        ___qtablewidgetitem18 = self.databaseInfoTable.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        self.twMachineTabs.setTabText(self.twMachineTabs.indexOf(self.databaseTab), QCoreApplication.translate("MainWindow", u"Database: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.tableName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter table name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Comment:", None))
        self.tableTabs.setTabText(self.tableTabs.indexOf(self.tableTabsBasic), QCoreApplication.translate("MainWindow", u"Basic", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Auto increment:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Default collation:", None))
        self.tableTabs.setTabText(self.tableTabs.indexOf(self.tableTabsOptions), QCoreApplication.translate("MainWindow", u"Options", None))
        self.addColumnButton_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeColumnButton_2.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.moveColumnUpButton_2.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.moveColumnDownButton_2.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        ___qtreewidgetitem1 = self.indexes.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Type / Length", None));
        self.tableTabs.setTabText(self.tableTabs.indexOf(self.tableTabsIndexes), QCoreApplication.translate("MainWindow", u"Indexes", None))
        self.tableTabs.setTabText(self.tableTabs.indexOf(self.createCode), QCoreApplication.translate("MainWindow", u"CREATE code", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Columns:", None))
        self.addColumnButton.setText(QCoreApplication.translate("MainWindow", u"Add Column", None))
        self.removeColumnButton.setText(QCoreApplication.translate("MainWindow", u"Remove Column", None))
        self.moveColumnUpButton.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.moveColumnDownButton.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        ___qtablewidgetitem19 = self.tableInfoTable.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem20 = self.tableInfoTable.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem21 = self.tableInfoTable.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Datatype", None));
        ___qtablewidgetitem22 = self.tableInfoTable.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Length/Set", None));
        ___qtablewidgetitem23 = self.tableInfoTable.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Unsigned", None));
        ___qtablewidgetitem24 = self.tableInfoTable.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Allow NULL", None));
        ___qtablewidgetitem25 = self.tableInfoTable.horizontalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Zerofill", None));
        ___qtablewidgetitem26 = self.tableInfoTable.horizontalHeaderItem(7)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Default", None));
        ___qtablewidgetitem27 = self.tableInfoTable.horizontalHeaderItem(8)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Comment", None));
        ___qtablewidgetitem28 = self.tableInfoTable.horizontalHeaderItem(9)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Collation", None));
        ___qtablewidgetitem29 = self.tableInfoTable.horizontalHeaderItem(10)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Expression", None));
        ___qtablewidgetitem30 = self.tableInfoTable.horizontalHeaderItem(11)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Virtuality", None));
        self.discardTableButton.setText(QCoreApplication.translate("MainWindow", u"Discard", None))
        self.saveTableButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.twMachineTabs.setTabText(self.twMachineTabs.indexOf(self.tableTab), QCoreApplication.translate("MainWindow", u"Table: ", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

