from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QShortcut
import MySQLdb
from database.database_server import DatabaseServer


class SessionManager(QtWidgets.QDialog):
    def __init__(self, mainApplicationWindow, configDb):
        super(SessionManager, self).__init__()

        self.conn = configDb
        # self.conn.row_factory = Row
        mainApplicationWindow.configDb = self.conn

        self.curs = self.conn.cursor()
        self.sessionIds = []

        self.initUI()
        self.loadSessionManager()
        # 主窗口
        self.mainApplicationWindow = mainApplicationWindow
        self.show()

    def initUI(self):
        self.labelNoSession = QtWidgets.QLabel('新用户吗? 为了连接一个MySQL服务器, 首先你得创建一个“会话”。只需要单击左下方的“新建”按钮来创建一个新的会话。\n\n给它起一个友好的名称（比如：“本地数据库服务器”）。这样你就能在下次启动HeidiSQL时能想起来。')
        self.labelNoSession.setWordWrap(True)
        
        # Setup input fields for settings tab
        checkCompressProtocol = QtWidgets.QCheckBox('Compressed client/server protocol')
        checkCompressProtocol.setEnabled(False)
        checkPasswordPrompt = QtWidgets.QCheckBox("Prompt")
        checkPasswordPrompt.setEnabled(False)
        comboDatabases = QtWidgets.QComboBox()
        comboDatabases.setEditable(True)
        comboDatabases.setEditText('Separated by semicolon')
        comboDatabases.setDisabled(True)
        self.comboNetworkType = QtWidgets.QComboBox(self)
        self.comboNetworkType.addItem('TCP/IP')
        self.spinPort = QtWidgets.QSpinBox()
        self.spinPort.setRange(0, 65535)
        self.spinPort.setMinimumWidth(65)
        self.textHostname = QtWidgets.QLineEdit()
        self.textPassword = QtWidgets.QLineEdit()
        self.textPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        textStartupScript = QtWidgets.QLineEdit()
        textStartupScript.setDisabled(True)
        self.textUser = QtWidgets.QLineEdit()
        
        # 创建服务器管理树
        self.treeServerManager = QtWidgets.QTreeWidget(self)
        self.treeServerManager.header().close()
        self.treeServerManager.setRootIsDecorated(False)
        self.treeServerManager.itemSelectionChanged.connect(self.slotServerSelectionChanged)
        
        # Layout for password text field and password check box
        layoutH6 = QtWidgets.QHBoxLayout()
        layoutH6.addWidget(self.textPassword)
        layoutH6.addWidget(checkPasswordPrompt)
        
        # Layout to smallimize the port input field
        layoutH7 = QtWidgets.QHBoxLayout()
        layoutH7.addWidget(self.spinPort)
        layoutH7.addStretch(1)
        
        # Setup the tab widget
        self.tabWidget = QtWidgets.QTabWidget(self)
        tabSettings = QtWidgets.QWidget()
        tabSettings.tabSettingsLayout = QtWidgets.QFormLayout(tabSettings)
        tabSettings.tabSettingsLayout.addRow('网络类型:', self.comboNetworkType)
        tabSettings.tabSettingsLayout.addRow('主机名 / IP:', self.textHostname)
        tabSettings.tabSettingsLayout.addRow('用户名:', self.textUser)
        tabSettings.tabSettingsLayout.addRow('密码:', layoutH6)
        tabSettings.tabSettingsLayout.addRow('端口:', layoutH7)
        tabSettings.tabSettingsLayout.addRow('', checkCompressProtocol)
        tabSettings.tabSettingsLayout.addRow('数据库:', comboDatabases)
        tabSettings.tabSettingsLayout.addRow('启动脚本:', textStartupScript)
        
        self.tabWidget.addTab(tabSettings, QtGui.QIcon("../resources/icons/wrench.png"), "设置")
        self.tabWidget.setVisible(False)
        
        # 创建按钮
        buttonNew = QtWidgets.QPushButton('新建')
        self.buttonSave = QtWidgets.QPushButton('保存')
        self.buttonSave.setDisabled(True)
        self.buttonDelete = QtWidgets.QPushButton('删除')
        self.buttonDelete.setDisabled(True)
        self.buttonOpen = QtWidgets.QPushButton('打开')
        self.buttonOpen.setDisabled(True)
        self.buttonCancel = QtWidgets.QPushButton('取消')
        
        # 会话管理底部的按钮布局
        layoutH4 = QtWidgets.QHBoxLayout()
        layoutH4.addWidget(buttonNew)
        layoutH4.addWidget(self.buttonSave)
        layoutH4.addWidget(self.buttonDelete)
        
        # 左侧会话管理器面板的布局
        layoutV1 = QtWidgets.QVBoxLayout()
        layoutV1.addWidget(QtWidgets.QLabel('已保存会话:'))
        layoutV1.addWidget(self.treeServerManager)
        layoutV1.addLayout(layoutH4)
        
        layoutH1 = QtWidgets.QHBoxLayout()
        layoutH1.addLayout(layoutV1)
        
        # 页签下面的 打开/取消 按钮的布局
        layoutH5 = QtWidgets.QHBoxLayout()
        layoutH5.addStretch(1);
        layoutH5.addWidget(self.buttonOpen)
        layoutH5.addWidget(self.buttonCancel)
        
        self.layoutV2 = QtWidgets.QVBoxLayout()
        self.layoutV2.addWidget(self.labelNoSession)
        self.layoutV2.addStretch(1)
        self.layoutV2.addLayout(layoutH5)
        
        # 区分会话管理器与页签面板的布局
        layoutH3 = QtWidgets.QHBoxLayout(self)
        layoutH3.addLayout(layoutH1)
        layoutH3.addLayout(self.layoutV2)
        layoutH3.setStretch(0, 30)
        layoutH3.setStretch(1, 70)
        
        # 信号设置
        buttonNew.clicked.connect(self.slotButtonNewClicked)
        # buttonCancel.clicked.connect(self.slotButtonCancelClicked)
        # self.buttonDelete.clicked.connect(self.slotButtonDeleteClicked)
        self.buttonOpen.clicked.connect(self.slotButtonOpenClicked)
        self.buttonSave.clicked.connect(self.slotButtonSaveClicked)

        self.textHostname.textEdited.connect(self.sessionModified)
        self.textUser.textEdited.connect(self.sessionModified)
        self.textPassword.textEdited.connect(self.sessionModified)
        self.spinPort.valueChanged.connect(self.sessionModified)

        # QShortcut("Ctrl+S", self, self.slotButtonSaveClicked)
        
        self.setLayout(layoutH3)

        self.setWindowTitle('会话管理器')
        self.setWindowIcon(QtGui.QIcon('../resources/icons/heidi.ico'))
        self.setModal(True)
        self.setGeometry(300, 300, 700, 400)


    def addNewServer(self):
        # Add new server to tree view
        newServer = QtWidgets.QTreeWidgetItem()
        newServer.setText(0, 'Unnamed')
        newServer.setIcon(0, QtGui.QIcon('../resources/icons/server_add.png'))
        newServer.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        
        self.sessionIds.append(None)
        self.treeServerManager.addTopLevelItem(newServer)
        self.treeServerManager.setCurrentItem(newServer)


    def toggleSettingsPane(self):
        if self.treeServerManager.topLevelItemCount() > 0:
            # Toggle settings window on - Settings窗口显示
            self.labelNoSession.setVisible(False)
            self.layoutV2.removeItem(self.layoutV2.itemAt(0))
            self.layoutV2.removeItem(self.layoutV2.itemAt(1))
            self.layoutV2.removeWidget(self.labelNoSession)
            self.layoutV2.insertWidget(0, self.tabWidget)
            self.layoutV2.setStretch(0, 1)
            self.tabWidget.setVisible(True)
            self.buttonDelete.setEnabled(True)
            self.buttonOpen.setEnabled(True)
            self.buttonSave.setEnabled(True)
        else:
            # Toggle settings window off and show the no sessions message
            self.labelNoSession.setVisible(True)
            self.layoutV2.removeWidget(self.tabWidget)
            self.layoutV2.insertSpacing(0, 17)
            self.layoutV2.insertWidget(1, self.labelNoSession)
            self.layoutV2.insertStretch(2, 1)
            self.tabWidget.setVisible(False)
            self.buttonDelete.setEnabled(False)
            self.buttonOpen.setEnabled(False)
            self.buttonSave.setEnabled(False)


    def slotButtonNewClicked(self):
        """
        新建按钮点击信号槽
        """
        self.addNewServer()
        self.toggleSettingsPane()


    def slotServerSelectionChanged(self):
        # 加载设置
        self.loadSettings()    


    def loadSettings(self):
        index = self.treeServerManager.indexOfTopLevelItem(self.treeServerManager.currentItem())

        settings = None
        if (index != -1):
            self.curs = self.conn.execute("SELECT * FROM sessions WHERE id = ?", [self.sessionIds[index]])
            settings = self.curs.fetchone()
            self.currentSessionData = settings
        
        if settings != None:
            self.textHostname.setText(settings['hostname'])
            self.textUser.setText(settings['username'])
            self.textPassword.setText(settings['password'])
            self.spinPort.setValue(settings['port'])
        else:
            # 如果没有保存的配置，则初始化
            self.initializeSessionData()

            self.textHostname.setText('127.0.0.1')
            self.textPassword.setText('123456');
            self.textUser.setText('root')
            self.spinPort.setValue(3306)


    def initializeSessionData(self):
        self.currentSessionData = {'hostname': '127.0.0.1', 'password': '123456', 'username': 'root', 'port': '3306'}


    def slotButtonOpenClicked(self):
        """
        打开按钮单击信号槽
        """
        session = self.getCurrentSession()
        applicationWindow = self.mainApplicationWindow

        try:
            dbServer = DatabaseServer(session['name'], applicationWindow, session['hostname'], session['username'], session['password'], session['port'])
            applicationWindow.show()
            applicationWindow.addDbServer(dbServer)
            self.hide()

        except MySQLdb._exceptions.OperationalError as e:
            message = "Connection Error : %s" % e
            QMessageBox.critical(self, 'Connection Error', message)


    def getCurrentSession(self):
        """
        获取当前会话信息
        """
        sessionIndex = self.treeServerManager.indexOfTopLevelItem(self.treeServerManager.currentItem())
        session = {
            'id': sessionIndex,
            'name': self.treeServerManager.currentItem().text(0),
            'network_type': self.comboNetworkType.currentIndex(),
            'hostname': self.textHostname.text(),
            'username': self.textUser.text(),
            'password': self.textPassword.text(),
            'port': self.spinPort.value(),
            'index': self.sessionIds[sessionIndex]
        }

        return session


    def loadSessionManager(self):
        """
        加载会话列表
        """
        try:
            self.curs = self.conn.execute("SELECT id, name FROM sessions")
        except OperationalError:
            self.createSessionsTable()
        
        for row in self.curs:
            newServer = QtWidgets.QTreeWidgetItem()
            newServer.setText(0, row['name'])
            # newServer.setIcon(0, QtGui.QIcon('../resources/icons/server.png'))
            # newServer.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)            
            
            self.treeServerManager.addTopLevelItem(newServer)
            self.sessionIds.append(row['id'])
            
        self.toggleSettingsPane()


    def slotButtonSaveClicked(self):
        """
        保存按钮单击信号槽
        """
        session = self.getCurrentSession()
        print(session)
        sessionName = session['name']
        sessionTreeItem = self.treeServerManager.currentItem()
        
        if sessionName[-1] == '*':
            sessionName = sessionName[:len(sessionName) - 2]

        if session['index'] is None:
            self.curs = self.conn.execute("SELECT name FROM sqlite_master WHERE Type='table' and name = 'sessions'")

            if self.curs.fetchone() is None:
                self.createSessionsTable()

            self.curs.execute(
                "INSERT INTO sessions (name, network_type, hostname, username, password, port) VALUES (?, ?, ?, ?, ?, ?)",
                    [
                        sessionName,
                        session['network_type'],
                        session['hostname'],
                        session['username'],
                        session['password'],
                        session['port']
                    ]
            )
        else:
            self.curs.execute(
                "UPDATE sessions SET name = ?, network_type = ?, hostname = ?, username = ?, password = ?, port = ? WHERE id = ?",
                    (
                        sessionName,
                        session['network_type'],
                        session['hostname'],
                        session['username'],
                        session['password'],
                        session['port'],
                        session['index']
                    )
            )
        self.conn.commit()

        self.buttonSave.setEnabled(False)
        sessionTreeItem.setText(0, sessionName)
        # Set server icon to unedited
        sessionTreeItem.setIcon(0, QtGui.QIcon('../resources/icons/server.png'))


    def sessionModified(self):
        """
        每当会话信息更改时调用
        """
        session = self.treeServerManager.currentItem();
        
        name = session.text(0)
        if (name[-2:] == ' *'):
            name = name[:len(name) - 2]

        # Check to see if session has been reverted back to normal or not to determine if we need to change the name
        if (
            self.textHostname.text() != self.currentSessionData['hostname'] or
            self.textPassword.text() != self.currentSessionData['password'] or
            self.textUser.text() != self.currentSessionData['username'] or
            self.spinPort.value() != self.currentSessionData['port']
        ):
            changed = True
        else:
            changed = False
            
        if (changed == True):
            # 如果会话信息有变动，则保存可用
            session.setText(0, name + ' *')
            self.buttonSave.setEnabled(True)
            session.setIcon(0, QtGui.QIcon('../resources/icons/server_edit.png'))
        else:
            session.setText(0, name)
            self.buttonSave.setEnabled(False)
            session.setIcon(0, QtGui.QIcon('../resources/icons/server.png'))