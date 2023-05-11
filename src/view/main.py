
from view.main_screen import Ui_MainWindow
from observer.file_selection_observable import File_Selection_Observable

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QResizeEvent,QPixmap, QIcon
from PyQt6.QtWidgets import QMainWindow, QProgressBar, QFileDialog

import pandas as pd

class Main (QMainWindow, Ui_MainWindow, File_Selection_Observable):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.resizeEvent = self.on_resize
        self.showMaximized()
        self.progressBar = QProgressBar()
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.statusBar().addWidget(self.progressBar)
        self.load_icons()
        self.actionOpen_file.triggered.connect(self.on_open_file)
        self.selected_file = None
        File_Selection_Observable.__init__(self)


    def on_resize(self, a0: QResizeEvent):
        size = a0.size()
        left = int(size.width() * 0.75)
        right = int(size.width() * 0.25)
        self.splitter_esq_dir.setGeometry(0, 0, size.width(), size.height())
        self.splitter_esq_dir.setSizes([left, right])
        self.label_visualization_area.setText(
            f'-> {size.width()}x{size.height()} -> 80%: {left} x 20%: {right} | {self.splitter_esq_dir.width()}x{self.splitter_esq_dir.height()}')
        super().resizeEvent(a0)

    def load_icons(self):
        img_up = QPixmap(r'img/setaUp.png').scaled(self.push_button_cima_treemap.width(),
                                 self.push_button_cima_treemap.height(),
                                    Qt.AspectRatioMode.KeepAspectRatio)
        self.push_button_cima_treemap.setIcon(QIcon(img_up))
        img_down = QPixmap(r'img/setaDown.png').scaled(self.push_button_baixo_treemap.width(),
                                    self.push_button_baixo_treemap.height(),
                                    Qt.AspectRatioMode.KeepAspectRatio)
        self.push_button_baixo_treemap.setIcon(QIcon(img_down))
        img_left = QPixmap(r'img/setaEsq.png').scaled(self.push_button_esquerda_treemap.width(),
                                    self.push_button_esquerda_treemap.height(),
                                    Qt.AspectRatioMode.KeepAspectRatio)
        self.push_button_esquerda_treemap.setIcon(QIcon(img_left))
        img_right = QPixmap(r'img/setaDir.png').scaled(self.push_button_direita_treemap.width(),
                                    self.push_button_direita_treemap.height(),
                                    Qt.AspectRatioMode.KeepAspectRatio)
        self.push_button_direita_treemap.setIcon(QIcon(img_right))
        self.setWindowIcon(QIcon(QPixmap(r'img\treemap_glyph_logo.png').scaled(32, 32)))

        icon = QIcon()
        icon.addPixmap(QPixmap(r"\img\folder.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionOpen_file.setIcon(icon)
    
    def on_open_file(self):        
        dialog = QFileDialog()
        dialog.fileSelected.connect(self.handle_file_selection)
        dialog.exec()

    def handle_file_selection(self, file_path):
        print(f'File selected: {file_path}')
        self.selected_file = file_path
        self.notify_file_selected(file_path)

    def closeEvent(self, event):
        self.notify_closing()


    @property
    def selected_file(self):
        return self.__selected_file
    
    @selected_file.setter
    def selected_file(self, selected_file):
        self.__selected_file = selected_file

       
    
