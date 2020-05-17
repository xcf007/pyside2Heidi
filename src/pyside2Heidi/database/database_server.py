import MySQLdb
import MySQLdb.cursors
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QTreeWidgetItem
from PySide2.QtSql import QSqlDatabase, QSqlQuery
from qthelpers.HeidiTreeWidgetItem import HeidiTreeWidgetItem
from .database import Database
import ctypes

class DatabaseServer:
    def __init__(self, name, applicationWindow, hostname, username, password, port):
        """
        @type name: str
        @type connection: MySQLdb.Connection
        @type applicationWindow: MainApplicationWindow
        """
        self.name = name
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.applicationWindow = applicationWindow
        self.databases = list()
        self.currentDatabase = None
        self.collations = list()

        ctypes.windll.LoadLibrary(r'D:\wamp64\bin\mysql\mysql5.7.21\lib\libmysql.dll')  # 加载驱动库
        self.connection = MySQLdb.connect(host = hostname, user = username, passwd = password, port = port, cursorclass = MySQLdb.cursors.DictCursor)
        db = QSqlDatabase.addDatabase('QMYSQL', name)
        db.setHostName(hostname)
        db.setUserName(username)
        db.setPassword(password)
        db.open()  # 打开数据库
        self.db = db

        serverItem = HeidiTreeWidgetItem()
        serverItem.setText(0, name)
        serverItem.setIcon(0, QIcon('../resources/icons/server.png'))
        serverItem.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        serverItem.setChildIndicatorPolicy(QTreeWidgetItem.DontShowIndicatorWhenChildless)
        serverItem.itemType = 'server'

        self.databaseTreeItem = serverItem

        applicationWindow.mainWindow.databaseTree.addTopLevelItem(serverItem)


    def execute(self, *args):
        """
        @type query: str
        @type params: list
        """
        query = QSqlQuery(db = self.db)
        query.prepare(args[0])
        if len(args) == 1:
            text = args[0]
        elif len(args) == 2:
            text = args[0] % args[1]
            for value in args[1]:
                query.addBindValue(value);

        query.exec_(args[0])

        statusWindow = self.applicationWindow.mainWindow.txtStatus
        # 状态窗口打印执行的SQL
        statusWindow.append("%s;" % text)

        return query

    def getDatabase(self, index):
        """
        @type index: int
        @rtype: Database
        """
        return self.databases(index)

    def reloadDatabases(self):
        query = self.execute('SHOW DATABASES')
        while query.next():
            databaseIndex = query.record().indexOf('Database')
            self.addDatabase(query.value(databaseIndex))
            # print(query.value(databaseIndex))

    def addDatabase(self, name):
        """
        @type server: DatabaseServer
        @type name: str
        """
        database = Database(self, name)
        self.databases.append(database)

    def refreshProcessList(self):
        """
        @type server: DatabaseServer
        """
        processListTree = self.applicationWindow.mainWindow.processListTree
        processListTree.clear()

        query = self.execute('SHOW FULL PROCESSLIST')

        numProcesses = 0
        while query.next():
            numProcesses += 1

            processItem = QTreeWidgetItem()
            processItem.setText(0, str(query.value(query.record().indexOf('Id'))))
            processItem.setText(1, str(query.value(query.record().indexOf('User'))))
            processItem.setText(2, str(query.value(query.record().indexOf('Host'))))
            processItem.setText(3, str(query.value(query.record().indexOf('db'))))
            processItem.setText(4, str(query.value(query.record().indexOf('Command'))))
            processItem.setText(5, str(query.value(query.record().indexOf('Time'))))
            processItem.setText(6, str(query.value(query.record().indexOf('State'))))
            processItem.setText(7, str(query.value(query.record().indexOf('Info'))))
            processListTree.addTopLevelItem(processItem)

        self.applicationWindow.mainWindow.processListTab.setTabText(0, "进程列表 (%d)" % numProcesses)

    def setCurrentDatabase(self, database):
        """
        @type database: Database
        """
        self.currentDatabase = database
        database.setAsCurrentDatabase()
        self.execute("USE `%s`" % database.name)

    def findDatabaseByName(self, name):
        """
        @type name: str
        @rtype: Database
        """
        for database in self.databases:
            if database.name == name:
                return database

    def getCollations(self):
        """
        @rtype: list
        """
        if len(self.collations) == 0:
            cursor = self.execute("SHOW COLLATION")
            while cursor.next():
                self.collations.append({'Collation': cursor.value(cursor.record().indexOf('Collation'))})

        return self.collations