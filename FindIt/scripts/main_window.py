from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
from findit import main as findit
from about_window import UiAboutWindow
import os

var = resources_rc


class AboutWindow(QtWidgets.QDialog, UiAboutWindow):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setup_ui(self)


class UiMainWindow(object):
    def __init__(self):
        self.actionAbout = None
        self.statusbar = None
        self.menuHelp = None
        self.menubar = None
        self.label_3 = None
        self.btn_choose_dir = None
        self.le_search_string = None
        self.le_data_dir = None
        self.label_2 = None
        self.btn_file_save = None
        self.label = None
        self.le_file_save = None
        self.gridLayout = None
        self.layoutWidget = None
        self.btn_findit = None
        self.gridLayout_2 = None
        self.gridLayoutWidget = None
        self.centralwidget = None
        self.search_string = None
        self.data_dir = None
        self.out_file = None

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 460, 761, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_findit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_findit.setObjectName("btn_findit")
        self.gridLayout_2.addWidget(self.btn_findit, 0, 1, 1, 1)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacer_item, 0, 0, 1, 1)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacer_item1, 0, 2, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 761, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.le_file_save = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_file_save.setObjectName("le_file_save")
        self.gridLayout.addWidget(self.le_file_save, 7, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btn_file_save = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_file_save.setObjectName("btn_file_save")
        self.gridLayout.addWidget(self.btn_file_save, 7, 2, 1, 1)
        spacer_item2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item2, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 3)
        self.le_data_dir = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_data_dir.setObjectName("le_data_dir")
        self.gridLayout.addWidget(self.le_data_dir, 4, 0, 1, 2)
        self.le_search_string = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_search_string.setObjectName("le_search_string")
        self.gridLayout.addWidget(self.le_search_string, 1, 0, 1, 1)
        self.btn_choose_dir = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_choose_dir.setObjectName("btn_choose_dir")
        self.gridLayout.addWidget(self.btn_choose_dir, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 3)
        spacer_item3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item3, 2, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(main_window)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.actionAbout.triggered.connect(self.open_about)
        self.btn_choose_dir.clicked.connect(self.choose_dir)
        self.btn_file_save.clicked.connect(self.save_file)
        self.btn_findit.clicked.connect(self.find_files)
        self.statusbar.showMessage("Ready")
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.setTabOrder(self.le_search_string, self.le_data_dir)
        main_window.setTabOrder(self.le_data_dir, self.btn_choose_dir)
        main_window.setTabOrder(self.btn_choose_dir, self.le_file_save)
        main_window.setTabOrder(self.le_file_save, self.btn_file_save)
        main_window.setTabOrder(self.btn_file_save, self.btn_findit)


    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "FindIt - By ACGI"))
        self.btn_findit.setText(_translate("MainWindow", "FindIt"))
        self.label.setText(_translate("MainWindow", "Search String"))
        self.btn_file_save.setText(_translate("MainWindow", "Choose Output Location"))
        self.label_2.setText(_translate("MainWindow", "Choose Data Directory"))
        self.btn_choose_dir.setText(_translate("MainWindow", "Choose Location"))
        self.label_3.setText(_translate("MainWindow", "Select Output Path"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    @staticmethod
    def open_about() -> None:
        dlg = AboutWindow()
        dlg.exec()

    def choose_dir(self) -> None:
        self.data_dir = QtWidgets.QFileDialog.getExistingDirectory(parent=None, caption="Choose Data Directory")
        self.le_data_dir.setText(self.data_dir)

    def save_file(self) -> None:
        self.out_file = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", "", "Text Files(*.txt)")
        self.le_file_save.setText(self.out_file[0])

    def find_files(self) -> None:
        self.search_string = self.le_search_string.text()
        try:
            if self.search_string == '':
                raise ValueError("Search string is required")
            if self.data_dir is None or self.le_data_dir == '':
                raise ValueError("Data directory is required")
            if not os.path.exists(self.data_dir):
                raise ValueError(f"{self.data_dir} does not exist")
            if self.out_file is None or self.out_file == '':
                raise ValueError("Output file is required")
            _find_dict = {
                '<string>': self.search_string,
                '<datadir>': self.data_dir,
                '<outputfile>': self.out_file[0]
            }
            self.statusbar.showMessage("Retrieving Information - Please wait...")
            QtWidgets.QApplication.processEvents()
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            findit(**_find_dict)
            QtWidgets.QApplication.restoreOverrideCursor()
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Success")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Retrieval Complete")
            msg.exec_()
            self.statusbar.showMessage("Ready")
        except ValueError as v:
            self.statusbar.showMessage(str(v))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
