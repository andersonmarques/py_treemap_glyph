import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QPixmap

from view.main import Main

class Visualization_Controller:
    def __init__(self):
        self.init_gui()

    # def on_open_app(self):
    #     print('Abrir aplicativo')
        
    # def on_exit_app(self, app):
    #     self.tray_icon.hide()
    #     app.quit()

    def init_gui(self):
        app = QApplication(sys.argv)
        # self.tray_icon = QSystemTrayIcon(parent=app)
        # self.tray_icon.setToolTip('Treemap Glyph')
        # self.tray_icon.setIcon(QIcon(QPixmap(r'img\treemap_glyph_logo.png').scaled(16, 16)))
        
        # self.menu = QMenu()
        # self.menu.addAction("Abrir aplicativo", self.on_open_app)
        # self.menu.addAction("Sair", lambda: self.on_exit_app(app))
        # self.tray_icon.setContextMenu(self.menu)
        
        # self.tray_icon.show()
        # app.setWindowIcon(QIcon(QPixmap(r'img\treemap_glyph_logo.png').scaled(32, 32)))
        self.__main_view = Main()
        self.__main_view.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    controller = Visualization_Controller()
   