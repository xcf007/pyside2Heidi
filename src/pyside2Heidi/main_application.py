import sys
import os
import PySide2
from PySide2 import QtWidgets
import sqlite3
from main_application_window import MainApplicationWindow
from session_manager import SessionManager
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.dirname(PySide2.__file__) + '/plugins/platforms'


class MainApplication:

    configDb = None

    def __init__(self):
        super().__init__()
        
        self.configDb = sqlite3.connect('../userdata.db')
        configDb = self.configDb
        configDb.row_factory = sqlite3.Row
        cursor = configDb.cursor()

        # 确保设置表始终存在，如果不存在则创建
        cursor.execute("SELECT name FROM sqlite_master WHERE Type='table' and name = 'settings'")
        if cursor.fetchone() is None:
            # 如果还没有保存过设置则创建设置表
            self.createSettingsTable()

        app = QtWidgets.QApplication(sys.argv)

        # 主窗口
        mainApplicationWindow = MainApplicationWindow(configDb)
        mainApplicationWindow.hide()

        # 会话管理器
        sessionManager = SessionManager(mainApplicationWindow, configDb)
        # self.sessionManager = sessionManager

        app.exec_()


    def createSettingsTable(self):
        """
        创建配置表
        """
        cursor = self.configDb.cursor()
        cursor.execute("""
            CREATE TABLE settings(
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                value TEXT
            );
        """)

        self.configDb.commit()        