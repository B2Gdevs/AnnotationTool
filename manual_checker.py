# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manual_checker.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QIntValidator
import os
import pickle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(550, 0, 321, 561))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.image_dir_button = QtWidgets.QToolButton(self.formLayoutWidget)
        self.image_dir_button.setObjectName("image_dir_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.image_dir_button)
        self.image_dir_line = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.image_dir_line.setObjectName("image_dir_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.image_dir_line)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.output_dir_button = QtWidgets.QToolButton(self.formLayoutWidget)
        self.output_dir_button.setObjectName("output_dir_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.output_dir_button)
        self.output_dir_line = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.output_dir_line.setObjectName("output_dir_line")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.output_dir_line)
        self.good_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.good_button.setStyleSheet("background-color:green\n"
"")
        self.good_button.setObjectName("good_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.good_button)
        self.bad_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.bad_button.setStyleSheet("background-color:rgb(239, 41, 41)")
        self.bad_button.setObjectName("bad_button")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.bad_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.previous_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.previous_button.setObjectName("previous_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.previous_button)
        self.next_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.next_button.setObjectName("next_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.next_button)
        self.image_counter_line = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.image_counter_line.setObjectName("image_counter_line")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.image_counter_line)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.total_images_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.total_images_label.setObjectName("total_images_label")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.total_images_label)
        self.image_setter = QtWidgets.QLabel(self.centralwidget)
        self.image_setter.setGeometry(QtCore.QRect(140, 190, 67, 17))
        self.image_setter.setObjectName("image_setter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Image_dir"))
        self.image_dir_button.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "output_dir"))
        self.output_dir_button.setText(_translate("MainWindow", "..."))
        self.good_button.setText(_translate("MainWindow", "Good Image"))
        self.bad_button.setText(_translate("MainWindow", "Bad Image"))
        self.previous_button.setText(_translate("MainWindow", "Previous Image"))
        self.next_button.setText(_translate("MainWindow", "Next Image"))
        self.label_3.setText(_translate("MainWindow", "Image #"))
        self.total_images_label.setText(_translate("MainWindow", "Out of # images"))
        self.image_setter.setText(_translate("MainWindow", "Image"))


        # self.image_counter_line.setValidator(QIntValidator())

        self.image_setter.setStyleSheet("background-color: green")
        self.image_setter.setGeometry(0,0, 500, 500)
        self.image_setter.setScaledContents(True)

        self.paths = None
        self.image_counter = 0

        try:
            self.load_checkpoint()
            self.update_visual_counter()
            message_box = QMessageBox(self.centralwidget)
            message_box.setText("Amount of images checked so far is {}".format(self.image_counter))
            message_box.show()
        except:
            message_box = QMessageBox(self.centralwidget)
            message_box.setText("Could not load checkpoint")
            message_box.show()
            self.checkpoint = 0
            


        self.image_dir_button.clicked.connect(self.image_dir)
        self.output_dir_button.clicked.connect(self.output_dir)
        self.good_button.clicked.connect(self.good_button_action)
        self.bad_button.clicked.connect(self.bad_button_action)

        self.previous_button.clicked.connect(self.previous_image)
        self.next_button.clicked.connect(self.next_image)

        self.image_counter_line.textChanged.connect(self.when_visual_counter_changed)
        


    def image_dir(self):
        try:
            filename= QFileDialog.getExistingDirectory(self.centralwidget, "Select an Image Directory to check")
            if filename:
                self.image_dir_line.setText(filename)
                self.paths = self.get_image_paths()
                self.total_images_label.setText("Out of {} images".format(len(self.paths)))
                if len(self.image_dir_line.text()) > 0 and len(self.output_dir_line.text()) > 0:
                    self.image_setter.setPixmap(QPixmap(self.paths[self.image_counter]))
                    if self.image_counter == 0:
                        self.image_counter_line.setText(str(1))
        except:
            pass

    def output_dir(self):
        try:
            filename= QFileDialog.getExistingDirectory(self.centralwidget, "Select a directory to store bad images")
            if filename:
                self.output_dir_line.setText(filename)
                if len(self.image_dir_line.text()) > 0 and len(self.output_dir_line.text()) > 0:
                    self.image_setter.setPixmap(QPixmap(self.paths[self.image_counter]))
                    if self.image_counter == 0:
                        self.image_counter_line.setText(str(1))
        except:
            pass

    def get_image_paths(self):

        image_root = self.image_dir_line.text()

        paths = [os.path.join(image_root, file) for file in os.listdir(image_root) if file.endswith((".jpg", ".png", ".jpeg"))]

        return paths

    def check_point(self):
        self.checkpoint = self.image_counter
        with open('checker_checkpoint.pickle', 'wb') as handle:
            pickle.dump(self.checkpoint, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_checkpoint(self):
        with open('checker_checkpoint.pickle', 'rb') as handle:
            self.checkpoint = pickle.load(handle)
            self.image_counter = self.checkpoint

    def good_button_action(self):
        self.image_counter += 1
        self.image_setter.setPixmap(QPixmap(self.paths[self.image_counter]))
        self.update_visual_counter()
        self.check_point()

    def bad_button_action(self):
        file_name = os.path.basename(self.paths[self.image_counter])
        new_path = os.path.join(self.output_dir_line.text(), file_name)
        os.rename(self.paths[self.image_counter], new_path)
        self.image_counter += 1
        self.image_setter.setPixmap(QPixmap(self.paths[self.image_counter]))
        self.update_visual_counter()
        self.check_point()

    def previous_image(self):
        self.image_counter -= 1
        self.image_setter.setPixmap(QPixmap(self.paths[self.image_counter]))
        self.update_visual_counter()
        self.check_point()

    def next_image(self):
        self.image_counter += 1
        self.image_setter.setPixmap(QPixmap(self.paths[self.image_counter]))
        self.update_visual_counter()
        self.check_point()

    def update_visual_counter(self):
        self.image_counter_line.setText(str(self.image_counter))
    
    def when_visual_counter_changed(self):
        try:
            self.image_counter = int(self.image_counter_line.text())
            self.image_setter.setPixmap(QPixmap(self.paths[self.image_counter]))
            self.check_point()
        except:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())