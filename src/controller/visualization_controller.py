import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QPixmap

import pandas as pd

from view.main import Main
from model.dao.file_model import File_Model
# from observer.file_observer import File_Observer

class Visualization_Controller:
    def __init__(self):
        self.file_model = File_Model()
        self.init_gui()

    def init_gui(self):
        app = QApplication(sys.argv)
        self.main_view = Main(controller=self, file_model=self.file_model)
        self.main_view.show()
        sys.exit(app.exec())

    def handle_file_selection(self, file_path):
        if file_path != None:
            self.file_model.notify_file_selected(file_path)

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    controller = Visualization_Controller()
   