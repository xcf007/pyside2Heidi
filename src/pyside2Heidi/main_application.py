import sys
import os
import PySide2
from PySide2 import QtWidgets
from session_manager import SessionManager
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.dirname(PySide2.__file__) + '/plugins/platforms'


class MainApplication:
    def __init__(self):
        super().__init__()
        app = QtWidgets.QApplication(sys.argv)
        sessionManager = SessionManager()
        self.sessionManager = sessionManager
        app.exec_()