from PySide2.QtWidgets import QMainWindow, QMenu
from ui.ui_mainwindow import Ui_MainWindow


class MainApplicationWindow(QMainWindow):
    def __init__(self, configDb):
        # self.obeyResize = False
        self.servers = []
        self.configDb = configDb

        QMainWindow.__init__(self)
        mainWindow = Ui_MainWindow()
        mainWindow.setupUi(self)

        # databaseInfoTable = mainWindow.databaseInfoTable
        # mainWindow.databaseTree.currentItemChanged.connect(self.updateDatabaseTreeSelection)
        # databaseInfoTable.horizontalHeader().sectionResized.connect(self.databaseTreeColumnResized)
        # mainWindow.databaseTree.itemExpanded.connect(self.databaseTreeItemExpanded)
        # mainWindow.txtStatus.setTextColor(QColor('darkBlue'))
        # mainWindow.twMachineTabs.removeTab(mainWindow.twMachineTabs.indexOf(mainWindow.databaseTab))
        # mainWindow.twMachineTabs.removeTab(mainWindow.twMachineTabs.indexOf(mainWindow.tableTab))

        # mainWindow.tableInfoTable.mainApplicationWindow = self

        # self.logHighlighter = MysqlSyntaxHighlighter(mainWindow.txtStatus.document())

        self.mainWindow = mainWindow
        # self.restoreSizePreferences()
        self.show()

        # self.tableTab = TableTab(self)
        # self.databaseTab = DatabaseTab(self)

        # self.closeEvent = self.onClose

        # databaseInfoTable.setContextMenuPolicy(Qt.CustomContextMenu)
        # databaseInfoTable.customContextMenuRequested.connect(self.databaseContextMenu)


    def addDbServer(self, server):
        pass