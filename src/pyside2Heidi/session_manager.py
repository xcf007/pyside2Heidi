from PySide2 import QtWidgets, QtGui, QtCore


class SessionManager(QtWidgets.QDialog):
    def __init__(self):
        super(SessionManager, self).__init__()
        self.sessionIds = []

        self.initUI()
        self.show()

    def initUI(self):
        self.labelNoSession = QtWidgets.QLabel('New here? In order to connect to a MySQL server, you have to create a so called "session" at first. Just click the "New" button on the bottom left to create your first session.\n\nGive it a friendly name (e.g. "Local DB Server") so you\'ll recall it the next time you start HeidiSQL.')
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
        
        # Create the Server Manager tree
        self.treeServerManager = QtWidgets.QTreeWidget(self)
        self.treeServerManager.header().close()
        self.treeServerManager.setRootIsDecorated(False)
        # self.treeServerManager.itemSelectionChanged.connect(self.slotServerSelectionChanged)
        
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
        buttonCancel = QtWidgets.QPushButton('取消')
        
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
        layoutH5.addWidget(buttonCancel)
        
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
        
        # Setup signals
        buttonNew.clicked.connect(self.slotButtonNewClicked)
        # buttonCancel.clicked.connect(self.slotButtonCancelClicked)
        # self.buttonDelete.clicked.connect(self.slotButtonDeleteClicked)
        # self.buttonOpen.clicked.connect(self.slotButtonOpenClicked)
        # self.buttonSave.clicked.connect(self.slotButtonSaveClicked)

        # self.textHostname.textEdited.connect(self.sessionModified)
        # self.textUser.textEdited.connect(self.sessionModified)
        # self.textPassword.textEdited.connect(self.sessionModified)
        # self.spinPort.valueChanged.connect(self.sessionModified)

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
            # self.layoutV2.setStretch(0, 1)
            # self.layoutV2.setStretch(1, 1)
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
        self.addNewServer()
        self.toggleSettingsPane()