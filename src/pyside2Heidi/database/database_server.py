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
        print('%s' % db.open() + '!!!!!!')

        self.db = db

        serverItem = HeidiTreeWidgetItem()
        serverItem.setText(0, name)
        serverItem.setIcon(0, QIcon('../resources/icons/server.png'))
        serverItem.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable)
        serverItem.setChildIndicatorPolicy(QTreeWidgetItem.DontShowIndicatorWhenChildless)
        serverItem.itemType = 'server'

        self.databaseTreeItem = serverItem

        applicationWindow.mainWindow.databaseTree.addTopLevelItem(serverItem)
        print('2#!!!!!!')

    def execute(self, *args):
        """
        @type query: str
        @type params: list
        """
        cursor = self.connection.cursor()
        query = QSqlQuery(self.db)
        query.prepare(args[0])
        if len(args) == 1:
            text = args[0]
        elif len(args) == 2:
            text = args[0] % args[1]
            for value in args[1]:
                query.addBindValue(value);

        query.exec(args[0])

        statusWindow = self.applicationWindow.mainWindow.txtStatus
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
            print(query.value(databaseIndex))

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

        cursor = self.execute('SHOW FULL PROCESSLIST')

        numProcesses = 0
        # for row in cursor:
        while cursor.next():
            numProcesses += 1

            # for value in row:
            #     if row[value] is None:
            #         row[value] = ''
            #     elif type(row[value] != str):
            #         row[value] = str(row[value])

            processItem = QTreeWidgetItem()
            processItem.setText(0, str(cursor.value(cursor.record().indexOf('Id'))))
            processItem.setText(1, str(cursor.value(cursor.record().indexOf('User'))))
            processItem.setText(2, str(cursor.value(cursor.record().indexOf('Host'))))
            processItem.setText(3, str(cursor.value(cursor.record().indexOf('db'))))
            processItem.setText(4, str(cursor.value(cursor.record().indexOf('Command'))))
            processItem.setText(5, str(cursor.value(cursor.record().indexOf('Time'))))
            processItem.setText(6, str(cursor.value(cursor.record().indexOf('State'))))
            processItem.setText(7, str(cursor.value(cursor.record().indexOf('Info'))))
            processListTree.addTopLevelItem(processItem)

        self.applicationWindow.mainWindow.processListTab.setTabText(0, "Process List (%d)" % numProcesses)

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
            for collation in cursor:
                self.collations.append(collation)

        return self.collations
