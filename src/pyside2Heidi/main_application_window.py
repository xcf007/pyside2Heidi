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
        # 左侧数据库Tree展开处理
        mainWindow.databaseTree.itemExpanded.connect(self.databaseTreeItemExpanded)
        databaseInfoTable.horizontalHeader().sectionResized.connect(self.databaseTreeColumnResized)
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

        self.closeEvent = self.onClose

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
            # 如果选择的服务器节点，则移除跟服务器不搭边的页签
            mainWindow = self.mainWindow
            mainWindow.twMachineTabs.removeTab(mainWindow.twMachineTabs.indexOf(mainWindow.databaseTab))
            mainWindow.twMachineTabs.removeTab(mainWindow.twMachineTabs.indexOf(mainWindow.tableTab))

            # 初始化机器页签
            machineTab = self.mainWindow.machineTab
            twMachineTabs = self.mainWindow.twMachineTabs
            twMachineTabs.setTabText(twMachineTabs.indexOf(machineTab), "主机: %s" % currentItem.text(0))
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
        """
        显示数据库页签
        """
        self.showTab(self.mainWindow.databaseTab, QIcon('../resources/icons/database.png'), 'Database:')

    def showTableTab(self):
        self.showTab(self.mainWindow.tableTab, QIcon('../resources/icons/table.png'), 'Table:')        

    def showTab(self, tab, name, icon):
        """
        @type tab: QTabWidget
        @type icon: QIcon
        @type name: str
        """
        self.mainWindow.twMachineTabs.addTab(tab, name, icon)

    def databaseTreeItemExpanded(self, item):
        """
        @type item: HeidiTreeWidgetItem
        """
        if item.itemType == 'database':
            # 遍历当前服务器的数据库找到当前指定的数据库
            database = self.currentServer.findDatabaseByName(item.text(0))
            if len(database.tables) == 0:
                database.refreshTables()


    def onClose(self, closeEvent):
        cursor = self.configDb.cursor()
        # 保存窗口位置
        cursor.execute("REPLACE INTO `settings` (name, value) VALUES ('mainwindow.x', ?), ('mainwindow.y', ?)", [self.pos().x(), self.pos().y()])

        sizes = self.mainWindow.splitter_2.sizes()
        for i, size in enumerate(sizes):
            cursor.execute("REPLACE INTO `settings` (name, value) VALUES ('splitter_2.%d', ?)" % i, [size])

        indexSize = self.mainWindow.indexes.columnWidth(0)
        cursor.execute("REPLACE INTO `settings` (name, value) VALUES ('tableIndexes.columnWidth', ?)", [indexSize])

        self.configDb.commit()

        QMainWindow.closeEvent(self, closeEvent)

    def databaseTreeColumnResized(self, index, previousWidth, width):
        # Last item auto stretches to take up the rest of the table
        if index != 7:
            cursor = self.configDb.cursor()
            cursor.execute("REPLACE INTO `settings` (name, value) VALUES ('databaseinfotable.%d.width', ?)" % index, [width])        