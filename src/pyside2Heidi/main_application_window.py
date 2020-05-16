from PySide2.QtWidgets import QMainWindow, QMenu
from PySide2.QtGui import QIcon
from ui.ui_mainwindow import Ui_MainWindow
from ui.main_window.table_tab import TableTab
from ui.main_window.database_tab import DatabaseTab


class MainApplicationWindow(QMainWindow):
    def __init__(self, configDb):
        # self.obeyResize = False
        self.servers = []
        self.configDb = configDb

        QMainWindow.__init__(self)
        mainWindow = Ui_MainWindow()
        mainWindow.setupUi(self)

        databaseInfoTable = mainWindow.databaseInfoTable
        mainWindow.databaseTree.currentItemChanged.connect(self.updateDatabaseTreeSelection)
        # databaseInfoTable.horizontalHeader().sectionResized.connect(self.databaseTreeColumnResized)
        # mainWindow.databaseTree.itemExpanded.connect(self.databaseTreeItemExpanded)
        # mainWindow.txtStatus.setTextColor(QColor('darkBlue'))
        mainWindow.twMachineTabs.removeTab(mainWindow.twMachineTabs.indexOf(mainWindow.databaseTab))
        mainWindow.twMachineTabs.removeTab(mainWindow.twMachineTabs.indexOf(mainWindow.tableTab))

        mainWindow.tableInfoTable.mainApplicationWindow = self

        # self.logHighlighter = MysqlSyntaxHighlighter(mainWindow.txtStatus.document())

        self.mainWindow = mainWindow
        # self.restoreSizePreferences()
        self.show()

        self.tableTab = TableTab(self)
        self.databaseTab = DatabaseTab(self)

        # self.closeEvent = self.onClose

        # databaseInfoTable.setContextMenuPolicy(Qt.CustomContextMenu)
        # databaseInfoTable.customContextMenuRequested.connect(self.databaseContextMenu)


    def addDbServer(self, server):
        """
        @type server: DatabaseServer
        """
        self.servers.append(server)
        self.currentServer = server
        server.reloadDatabases()
        server.refreshProcessList()

    def updateDatabaseTreeSelection(self, currentItem, previousItem):
        """
        @type currentItem: HeidiTreeWidgetItem
        @type previousItem: HeidiTreeWidgetItem
        """
        if currentItem.itemType == 'database':
            # 如果单击的是数据库则更新当前数据，如：USE `db`
            self.updateCurrentDatabase(currentItem)
        elif currentItem.itemType == 'server':
            # Remove any tabs not dealing with server specific stuff
            mainWindow = self.mainWindow
            mainWindow.twMachineTabs.removeTab(mainWindow.twMachineTabs.indexOf(mainWindow.databaseTab))
            mainWindow.twMachineTabs.removeTab(mainWindow.twMachineTabs.indexOf(mainWindow.tableTab))

            # Initialize the machine tab
            machineTab = self.mainWindow.machineTab
            twMachineTabs = self.mainWindow.twMachineTabs
            twMachineTabs.setTabText(twMachineTabs.indexOf(machineTab), "Host: %s" % currentItem.text(0))
            twMachineTabs.setCurrentWidget(self.mainWindow.machineTab)
        elif currentItem.itemType == 'table':
            self.updateCurrentDatabase(currentItem.parent())
            self.showTableTab()
            tableName = currentItem.text(0)
            self.currentDatabase.setCurrentTable(self.currentDatabase.findTableByName(tableName))

    def updateCurrentDatabase(self, databaseTreeItem):
        """
        @type databaseTreeItem: HeidiTreeWidgetItem
        """
        dbName = databaseTreeItem.text(0)
        server = self.getServer(0)
        database = server.findDatabaseByName(dbName)
        self.currentDatabase = database
        server.setCurrentDatabase(database)

    def getServer(self, index):
        """
        @type index: int
        @rtype: DatabaseServer
        """
        return self.servers[index]

    def showDatabaseTab(self):
        self.showTab(self.mainWindow.databaseTab, QIcon('../resources/icons/database.png'), 'Database:')

    def showTab(self, tab, name, icon):
        """
        @type tab: QTabWidget
        @type icon: QIcon
        @type name: str
        """
        self.mainWindow.twMachineTabs.addTab(tab, name, icon)