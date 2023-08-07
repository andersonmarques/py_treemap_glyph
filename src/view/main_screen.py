# Form implementation generated from reading ui file 'main_screen.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1328, 839)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_esq_dir = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_esq_dir.setGeometry(QtCore.QRect(0, 0, 1291, 781))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_esq_dir.sizePolicy().hasHeightForWidth())
        self.splitter_esq_dir.setSizePolicy(sizePolicy)
        self.splitter_esq_dir.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_esq_dir.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_esq_dir.setObjectName("splitter_esq_dir")
        self.frame_visualization = QtWidgets.QFrame(parent=self.splitter_esq_dir)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_visualization.sizePolicy().hasHeightForWidth())
        self.frame_visualization.setSizePolicy(sizePolicy)
        self.frame_visualization.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_visualization.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.frame_visualization.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_visualization.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_visualization.setObjectName("frame_visualization")
        self.label_visualization_area = QtWidgets.QLabel(parent=self.frame_visualization)
        self.label_visualization_area.setGeometry(QtCore.QRect(0, 60, 621, 481))
        self.label_visualization_area.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.label_visualization_area.setText("")
        self.label_visualization_area.setObjectName("label_visualization_area")
        self.frame_settings = QtWidgets.QFrame(parent=self.splitter_esq_dir)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_settings.sizePolicy().hasHeightForWidth())
        self.frame_settings.setSizePolicy(sizePolicy)
        self.frame_settings.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_settings.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_settings.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_settings.setObjectName("frame_settings")
        self.splitter_up_down = QtWidgets.QSplitter(parent=self.frame_settings)
        self.splitter_up_down.setGeometry(QtCore.QRect(10, 10, 391, 761))
        self.splitter_up_down.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_up_down.setObjectName("splitter_up_down")
        self.frame_settings_up = QtWidgets.QFrame(parent=self.splitter_up_down)
        self.frame_settings_up.setEnabled(True)
        self.frame_settings_up.setMaximumSize(QtCore.QSize(16777215, 315))
        self.frame_settings_up.setAutoFillBackground(False)
        self.frame_settings_up.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_settings_up.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_settings_up.setObjectName("frame_settings_up")
        self.tab_widget_abas = QtWidgets.QTabWidget(parent=self.frame_settings_up)
        self.tab_widget_abas.setGeometry(QtCore.QRect(0, 10, 391, 301))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setKerning(False)
        self.tab_widget_abas.setFont(font)
        self.tab_widget_abas.setObjectName("tab_widget_abas")
        self.tab_treemap = QtWidgets.QWidget()
        self.tab_treemap.setObjectName("tab_treemap")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.tab_treemap)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 261))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 8, 1, 1, 2)
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_3.addWidget(self.comboBox_3, 7, 1, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_3.addWidget(self.comboBox_2, 6, 1, 1, 2)
        self.comboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 5, 1, 1, 2)
        self.listWidget = QtWidgets.QListWidget(parent=self.formLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_3.addWidget(self.listWidget, 1, 0, 3, 1)
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.formLayoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_3.addWidget(self.listWidget_2, 1, 2, 3, 1)
        self.push_button_cima_treemap = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.push_button_cima_treemap.setText("")
        self.push_button_cima_treemap.setObjectName("push_button_cima_treemap")
        self.gridLayout_3.addWidget(self.push_button_cima_treemap, 1, 3, 1, 1)
        self.push_button_direita_treemap = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.push_button_direita_treemap.setText("")
        self.push_button_direita_treemap.setObjectName("push_button_direita_treemap")
        self.gridLayout_3.addWidget(self.push_button_direita_treemap, 1, 1, 1, 1)
        self.push_button_esquerda_treemap = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.push_button_esquerda_treemap.setText("")
        self.push_button_esquerda_treemap.setObjectName("push_button_esquerda_treemap")
        self.gridLayout_3.addWidget(self.push_button_esquerda_treemap, 3, 1, 1, 1)
        self.push_button_baixo_treemap = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.push_button_baixo_treemap.setText("")
        self.push_button_baixo_treemap.setObjectName("push_button_baixo_treemap")
        self.gridLayout_3.addWidget(self.push_button_baixo_treemap, 3, 3, 1, 1)
        self.tab_widget_abas.addTab(self.tab_treemap, "")
        self.tab_grid = QtWidgets.QWidget()
        self.tab_grid.setObjectName("tab_grid")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_grid)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 371, 261))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.formLayoutWidget_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.formLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_7.addWidget(self.pushButton_3, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 2, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(parent=self.formLayoutWidget_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_7.addWidget(self.checkBox_5, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 1)
        self.push_button_view_grid = QtWidgets.QPushButton(parent=self.formLayoutWidget_2)
        self.push_button_view_grid.setObjectName("push_button_view_grid")
        self.gridLayout_7.addWidget(self.push_button_view_grid, 8, 1, 1, 2)
        self.comboBox_11 = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.comboBox_11.setObjectName("comboBox_11")
        self.gridLayout_7.addWidget(self.comboBox_11, 7, 1, 1, 2)
        self.comboBox_12 = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.comboBox_12.setObjectName("comboBox_12")
        self.gridLayout_7.addWidget(self.comboBox_12, 6, 1, 1, 2)
        self.comboBox_13 = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.comboBox_13.setObjectName("comboBox_13")
        self.gridLayout_7.addWidget(self.comboBox_13, 5, 1, 1, 2)
        self.listWidget_7 = QtWidgets.QListWidget(parent=self.formLayoutWidget_2)
        self.listWidget_7.setObjectName("listWidget_7")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_7.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_7.addItem(item)
        self.gridLayout_7.addWidget(self.listWidget_7, 1, 0, 3, 1)
        self.listWidget_8 = QtWidgets.QListWidget(parent=self.formLayoutWidget_2)
        self.listWidget_8.setObjectName("listWidget_8")
        self.gridLayout_7.addWidget(self.listWidget_8, 1, 2, 3, 1)
        self.push_button_cima_grid = QtWidgets.QPushButton(parent=self.formLayoutWidget_2)
        self.push_button_cima_grid.setText("")
        self.push_button_cima_grid.setObjectName("push_button_cima_grid")
        self.gridLayout_7.addWidget(self.push_button_cima_grid, 1, 3, 1, 1)
        self.push_button_direita_gird = QtWidgets.QPushButton(parent=self.formLayoutWidget_2)
        self.push_button_direita_gird.setText("")
        self.push_button_direita_gird.setObjectName("push_button_direita_gird")
        self.gridLayout_7.addWidget(self.push_button_direita_gird, 1, 1, 1, 1)
        self.push_button_esquerda_grid = QtWidgets.QPushButton(parent=self.formLayoutWidget_2)
        self.push_button_esquerda_grid.setText("")
        self.push_button_esquerda_grid.setObjectName("push_button_esquerda_grid")
        self.gridLayout_7.addWidget(self.push_button_esquerda_grid, 3, 1, 1, 1)
        self.push_button_baixo_grid = QtWidgets.QPushButton(parent=self.formLayoutWidget_2)
        self.push_button_baixo_grid.setText("")
        self.push_button_baixo_grid.setObjectName("push_button_baixo_grid")
        self.gridLayout_7.addWidget(self.push_button_baixo_grid, 3, 3, 1, 1)
        self.tab_widget_abas.addTab(self.tab_grid, "")
        self.tab_categorical_glyph = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tab_categorical_glyph.setFont(font)
        self.tab_categorical_glyph.setObjectName("tab_categorical_glyph")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_categorical_glyph)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 387, 280))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_7 = QtWidgets.QComboBox(parent=self.gridLayoutWidget_3)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_4.addWidget(self.comboBox_7, 5, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 2, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(parent=self.gridLayoutWidget_3)
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_4.addWidget(self.comboBox_9, 7, 3, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.gridLayoutWidget_3)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_4.addWidget(self.comboBox_5, 5, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_4.addWidget(self.pushButton_9, 2, 3, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.gridLayoutWidget_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_4.addWidget(self.comboBox_4, 6, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_4.addWidget(self.pushButton_10, 3, 3, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(parent=self.gridLayoutWidget_3)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_4.addWidget(self.comboBox_6, 7, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(parent=self.gridLayoutWidget_3)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout_4.addWidget(self.listWidget_3, 2, 0, 2, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.gridLayoutWidget_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_4.addWidget(self.checkBox_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)
        self.listView = QtWidgets.QListView(parent=self.gridLayoutWidget_3)
        self.listView.setObjectName("listView")
        self.gridLayout_4.addWidget(self.listView, 2, 2, 2, 1)
        self.comboBox_8 = QtWidgets.QComboBox(parent=self.gridLayoutWidget_3)
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout_4.addWidget(self.comboBox_8, 6, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_4.addWidget(self.pushButton_11, 8, 2, 1, 2)
        self.tab_widget_abas.addTab(self.tab_categorical_glyph, "")
        self.tab_continuous_glyph = QtWidgets.QWidget()
        self.tab_continuous_glyph.setObjectName("tab_continuous_glyph")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab_continuous_glyph)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 387, 231))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_5.addWidget(self.pushButton_13, 3, 1, 1, 1)
        self.listView_2 = QtWidgets.QListView(parent=self.gridLayoutWidget_4)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout_5.addWidget(self.listView_2, 2, 0, 2, 1)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_5.addWidget(self.pushButton_12, 2, 1, 1, 1)
        self.listWidget_4 = QtWidgets.QListWidget(parent=self.gridLayoutWidget_4)
        self.listWidget_4.setObjectName("listWidget_4")
        self.gridLayout_5.addWidget(self.listWidget_4, 2, 2, 2, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.gridLayoutWidget_4)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_5.addWidget(self.pushButton_15, 2, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_5.addWidget(self.pushButton_16, 3, 3, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(parent=self.gridLayoutWidget_4)
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout_5.addWidget(self.comboBox_10, 0, 1, 1, 2)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_5.addWidget(self.pushButton_14, 4, 0, 1, 4)
        self.tab_widget_abas.addTab(self.tab_continuous_glyph, "")
        self.tab_details = QtWidgets.QWidget()
        self.tab_details.setObjectName("tab_details")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(parent=self.tab_details)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 371, 251))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.gridLayoutWidget_5)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_6.addWidget(self.checkBox_4, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)
        self.listWidget_6 = QtWidgets.QListWidget(parent=self.gridLayoutWidget_5)
        self.listWidget_6.setObjectName("listWidget_6")
        self.gridLayout_6.addWidget(self.listWidget_6, 2, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_6.addWidget(self.pushButton_17, 2, 1, 1, 1)
        self.listWidget_5 = QtWidgets.QListWidget(parent=self.gridLayoutWidget_5)
        self.listWidget_5.setObjectName("listWidget_5")
        self.gridLayout_6.addWidget(self.listWidget_5, 2, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_6.addWidget(self.pushButton_18, 3, 1, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_6.addWidget(self.pushButton_19, 4, 0, 1, 3)
        self.tab_widget_abas.addTab(self.tab_details, "")
        self.tab__filter = QtWidgets.QWidget()
        self.tab__filter.setObjectName("tab__filter")
        self.tab_widget_abas.addTab(self.tab__filter, "")
        self.frame_legend_down = QtWidgets.QFrame(parent=self.splitter_up_down)
        self.frame_legend_down.setStyleSheet("background-color: rgb(180, 173, 172);")
        self.frame_legend_down.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_legend_down.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_legend_down.setObjectName("frame_legend_down")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1328, 26))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(parent=self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuAdaptive_Glyph = QtWidgets.QMenu(parent=self.menubar)
        self.menuAdaptive_Glyph.setObjectName("menuAdaptive_Glyph")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open_file = QtGui.QAction(parent=MainWindow)
        self.action_open_file.setObjectName("action_open_file")
        self.actionActivate = QtGui.QAction(parent=MainWindow)
        self.actionActivate.setObjectName("actionActivate")
        self.actionScreenshot = QtGui.QAction(parent=MainWindow)
        self.actionScreenshot.setObjectName("actionScreenshot")
        self.actionVersion = QtGui.QAction(parent=MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.action_treemap = QtGui.QAction(parent=MainWindow)
        self.action_treemap.setObjectName("action_treemap")
        self.action_grid = QtGui.QAction(parent=MainWindow)
        self.action_grid.setObjectName("action_grid")
        self.menuFIle.addAction(self.action_open_file)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.action_treemap)
        self.menuFIle.addAction(self.action_grid)
        self.menuAdaptive_Glyph.addAction(self.actionActivate)
        self.menuAbout.addAction(self.actionScreenshot)
        self.menuAbout.addAction(self.actionVersion)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuAdaptive_Glyph.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_widget_abas.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Treemap Glyphs"))
        self.pushButton.setText(_translate("MainWindow", "Color:"))
        self.label_2.setText(_translate("MainWindow", "Size:"))
        self.label_3.setText(_translate("MainWindow", "Group Hierarchy:"))
        self.checkBox.setText(_translate("MainWindow", "Label:"))
        self.label.setText(_translate("MainWindow", "Avaliable Attributes:"))
        self.pushButton_2.setText(_translate("MainWindow", "View Treemap"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "teste"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "teste2"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tab_widget_abas.setTabText(self.tab_widget_abas.indexOf(self.tab_treemap), _translate("MainWindow", "Treemap"))
        self.pushButton_3.setText(_translate("MainWindow", "Color:"))
        self.label_8.setText(_translate("MainWindow", "Size:"))
        self.label_9.setText(_translate("MainWindow", "Selected Attributes:"))
        self.checkBox_5.setText(_translate("MainWindow", "Label:"))
        self.label_10.setText(_translate("MainWindow", "Avaliable Attributes:"))
        self.push_button_view_grid.setText(_translate("MainWindow", "View Grid"))
        __sortingEnabled = self.listWidget_7.isSortingEnabled()
        self.listWidget_7.setSortingEnabled(False)
        item = self.listWidget_7.item(0)
        item.setText(_translate("MainWindow", "teste"))
        item = self.listWidget_7.item(1)
        item.setText(_translate("MainWindow", "teste2"))
        self.listWidget_7.setSortingEnabled(__sortingEnabled)
        self.tab_widget_abas.setTabText(self.tab_widget_abas.indexOf(self.tab_grid), _translate("MainWindow", "Grid"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.tab_widget_abas.setTabText(self.tab_widget_abas.indexOf(self.tab_categorical_glyph), _translate("MainWindow", "Categorial Glyph"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_16.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.tab_widget_abas.setTabText(self.tab_widget_abas.indexOf(self.tab_continuous_glyph), _translate("MainWindow", "Continuous Glyph"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_17.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_18.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_19.setText(_translate("MainWindow", "PushButton"))
        self.tab_widget_abas.setTabText(self.tab_widget_abas.indexOf(self.tab_details), _translate("MainWindow", "Details"))
        self.tab_widget_abas.setTabText(self.tab_widget_abas.indexOf(self.tab__filter), _translate("MainWindow", "Filter"))
        self.menuFIle.setTitle(_translate("MainWindow", "File"))
        self.menuAdaptive_Glyph.setTitle(_translate("MainWindow", "Adaptive Glyph"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.action_open_file.setText(_translate("MainWindow", "Open file"))
        self.actionActivate.setText(_translate("MainWindow", "Activate"))
        self.actionScreenshot.setText(_translate("MainWindow", "Screenshot"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
        self.action_treemap.setText(_translate("MainWindow", "Treemap"))
        self.action_grid.setText(_translate("MainWindow", "Grid"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
