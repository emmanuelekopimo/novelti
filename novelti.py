
import pygame
import pygame.camera as pygamecamera
import numpy 
import pyvirtualcam 
import cv2 
import time
import sys 
import itertools
from pygame.locals import *
from threading import Thread
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 604)
        MainWindow.setMinimumSize(QSize(850, 604))
        MainWindow.setMaximumSize(QSize(850, 604))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_11 = QGridLayout(self.groupBox_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.lineEdit_6 = QLineEdit(self.groupBox_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaxLength(12)

        self.gridLayout_11.addWidget(self.lineEdit_6, 0, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.groupBox_7)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_11.addWidget(self.pushButton_12, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_7, 1, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_2 = QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaxLength(12)

        self.gridLayout_6.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox_5)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_6.addWidget(self.pushButton_8, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_9 = QGridLayout(self.groupBox_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lineEdit_5 = QLineEdit(self.groupBox_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaxLength(12)

        self.gridLayout_9.addWidget(self.lineEdit_5, 0, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.groupBox_6)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_9.addWidget(self.pushButton_11, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_12 = QGridLayout(self.groupBox_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.lineEdit_7 = QLineEdit(self.groupBox_10)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaxLength(12)

        self.gridLayout_12.addWidget(self.lineEdit_7, 0, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.groupBox_10)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_12.addWidget(self.pushButton_13, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_10, 1, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_5.addWidget(self.pushButton_7, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_7 = QGridLayout(self.groupBox_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_3 = QLineEdit(self.groupBox_8)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaxLength(12)

        self.gridLayout_7.addWidget(self.lineEdit_3, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox_8)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_7.addWidget(self.pushButton_9, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_8, 0, 2, 1, 1)

        self.groupBox_9 = QGroupBox(self.groupBox_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_8 = QGridLayout(self.groupBox_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lineEdit_4 = QLineEdit(self.groupBox_9)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaxLength(12)

        self.gridLayout_8.addWidget(self.lineEdit_4, 0, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.groupBox_9)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_8.addWidget(self.pushButton_10, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_9, 0, 3, 1, 1)

        self.groupBox_14 = QGroupBox(self.groupBox_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_13 = QGridLayout(self.groupBox_14)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lineEdit_8 = QLineEdit(self.groupBox_14)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaxLength(12)

        self.gridLayout_13.addWidget(self.lineEdit_8, 0, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.groupBox_14)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_13.addWidget(self.pushButton_14, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_14, 1, 3, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 6)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.groupBox_11 = QGroupBox(self.centralwidget)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_4 = QGridLayout(self.groupBox_11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_18 = QGroupBox(self.groupBox_11)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_19 = QGridLayout(self.groupBox_18)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_16 = QLabel(self.groupBox_18)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_19.addWidget(self.label_16, 0, 0, 1, 1)

        self.spinBox_12 = QSpinBox(self.groupBox_18)
        self.spinBox_12.setObjectName(u"spinBox_12")

        self.gridLayout_19.addWidget(self.spinBox_12, 1, 0, 1, 1)

        self.pushButton_20 = QPushButton(self.groupBox_18)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout_19.addWidget(self.pushButton_20, 2, 0, 1, 2)

        self.label_17 = QLabel(self.groupBox_18)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_19.addWidget(self.label_17, 0, 1, 1, 1)

        self.spinBox_11 = QSpinBox(self.groupBox_18)
        self.spinBox_11.setObjectName(u"spinBox_11")

        self.gridLayout_19.addWidget(self.spinBox_11, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_18, 1, 2, 1, 1)

        self.groupBox_12 = QGroupBox(self.groupBox_11)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_14 = QGridLayout(self.groupBox_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_24 = QLabel(self.groupBox_12)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_14.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_12)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_14.addWidget(self.label_25, 0, 1, 1, 1)

        self.spinBox_10 = QSpinBox(self.groupBox_12)
        self.spinBox_10.setObjectName(u"spinBox_10")

        self.gridLayout_14.addWidget(self.spinBox_10, 1, 0, 1, 1)

        self.spinBox_9 = QSpinBox(self.groupBox_12)
        self.spinBox_9.setObjectName(u"spinBox_9")

        self.gridLayout_14.addWidget(self.spinBox_9, 1, 1, 1, 1)

        self.pushButton_24 = QPushButton(self.groupBox_12)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout_14.addWidget(self.pushButton_24, 2, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_12, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_11)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 0, 1, 1, 1)

        self.pushButton_22 = QPushButton(self.groupBox)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout_2.addWidget(self.pushButton_22, 2, 0, 1, 2)

        self.spinBox_15 = QSpinBox(self.groupBox)
        self.spinBox_15.setObjectName(u"spinBox_15")

        self.gridLayout_2.addWidget(self.spinBox_15, 1, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.spinBox_16 = QSpinBox(self.groupBox)
        self.spinBox_16.setObjectName(u"spinBox_16")

        self.gridLayout_2.addWidget(self.spinBox_16, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 3, 1, 1, 1)

        self.groupBox_17 = QGroupBox(self.groupBox_11)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.gridLayout_15 = QGridLayout(self.groupBox_17)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_8 = QLabel(self.groupBox_17)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_15.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_17)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_15.addWidget(self.label_9, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_17)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_15.addWidget(self.spinBox, 1, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox_17)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_15.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_17)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFrameShape(QFrame.StyledPanel)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_6, 2, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_17, 0, 0, 1, 1)

        self.groupBox_19 = QGroupBox(self.groupBox_11)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_20 = QGridLayout(self.groupBox_19)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_18 = QLabel(self.groupBox_19)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_20.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox_19)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_20.addWidget(self.label_19, 0, 1, 1, 1)

        self.spinBox_14 = QSpinBox(self.groupBox_19)
        self.spinBox_14.setObjectName(u"spinBox_14")

        self.gridLayout_20.addWidget(self.spinBox_14, 1, 0, 1, 1)

        self.spinBox_13 = QSpinBox(self.groupBox_19)
        self.spinBox_13.setObjectName(u"spinBox_13")

        self.gridLayout_20.addWidget(self.spinBox_13, 1, 1, 1, 1)

        self.pushButton_21 = QPushButton(self.groupBox_19)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout_20.addWidget(self.pushButton_21, 2, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_19, 3, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.groupBox_11)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_18 = QGridLayout(self.groupBox_15)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_14 = QLabel(self.groupBox_15)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_18.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_15)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_18.addWidget(self.label_15, 0, 1, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox_15)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.gridLayout_18.addWidget(self.spinBox_6, 1, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.groupBox_15)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.gridLayout_18.addWidget(self.spinBox_5, 1, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.groupBox_15)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout_18.addWidget(self.pushButton_19, 2, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_15, 0, 2, 1, 1)

        self.groupBox_13 = QGroupBox(self.groupBox_11)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_17 = QGridLayout(self.groupBox_13)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_12 = QLabel(self.groupBox_13)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_17.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_13)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_17.addWidget(self.label_13, 0, 1, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox_13)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout_17.addWidget(self.spinBox_4, 1, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox_13)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_17.addWidget(self.spinBox_3, 1, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.groupBox_13)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_17.addWidget(self.pushButton_18, 2, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_13, 0, 1, 1, 1)

        self.groupBox_16 = QGroupBox(self.groupBox_11)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_16 = QGridLayout(self.groupBox_16)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_10 = QLabel(self.groupBox_16)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_16.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_16)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_16.addWidget(self.label_11, 0, 1, 1, 1)

        self.spinBox_8 = QSpinBox(self.groupBox_16)
        self.spinBox_8.setObjectName(u"spinBox_8")

        self.gridLayout_16.addWidget(self.spinBox_8, 1, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.groupBox_16)
        self.spinBox_7.setObjectName(u"spinBox_7")

        self.gridLayout_16.addWidget(self.spinBox_7, 1, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.groupBox_16)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_16.addWidget(self.pushButton_17, 2, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_16, 1, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.groupBox_11)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_21 = QGridLayout(self.groupBox_20)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_22 = QLabel(self.groupBox_20)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_21.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_20)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_21.addWidget(self.label_23, 0, 1, 1, 1)

        self.spinBox_18 = QSpinBox(self.groupBox_20)
        self.spinBox_18.setObjectName(u"spinBox_18")

        self.gridLayout_21.addWidget(self.spinBox_18, 1, 0, 1, 1)

        self.spinBox_17 = QSpinBox(self.groupBox_20)
        self.spinBox_17.setObjectName(u"spinBox_17")

        self.gridLayout_21.addWidget(self.spinBox_17, 1, 1, 1, 1)

        self.pushButton_23 = QPushButton(self.groupBox_20)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout_21.addWidget(self.pushButton_23, 2, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_20, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_11, 2, 0, 1, 6)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 0, 5, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.gridLayout_10 = QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_3 = QGroupBox(self.frame_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(100, 16777215))
        self.gridLayout_23 = QGridLayout(self.groupBox_3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.lineEdit_11 = QLineEdit(self.groupBox_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMaxLength(3)

        self.gridLayout_23.addWidget(self.lineEdit_11, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.gridLayout_23.addWidget(self.label_5, 2, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaxLength(3)

        self.gridLayout_23.addWidget(self.lineEdit_10, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_23.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_3, 11, 0, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer, 3, 0, 1, 3)

        self.groupBox_22 = QGroupBox(self.frame_3)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_24 = QGridLayout(self.groupBox_22)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_7 = QLabel(self.groupBox_22)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_24.addWidget(self.label_7, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox_22)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_24.addWidget(self.comboBox_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_22)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_24.addWidget(self.label_3, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox_22)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_24.addWidget(self.comboBox, 3, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_22, 11, 1, 2, 1)

        self.groupBox_21 = QGroupBox(self.frame_3)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.gridLayout_22 = QGridLayout(self.groupBox_21)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.pushButton_15 = QPushButton(self.groupBox_21)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_22.addWidget(self.pushButton_15, 3, 0, 1, 2)

        self.label_26 = QLabel(self.groupBox_21)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_22.addWidget(self.label_26, 0, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox_21)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_22.addWidget(self.label_27, 1, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox_21)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMaxLength(11)
        self.lineEdit_12.setFrame(True)
        self.lineEdit_12.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_22.addWidget(self.lineEdit_12, 2, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox_21)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_22.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.groupBox_21)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaxLength(11)
        self.lineEdit_9.setFrame(True)
        self.lineEdit_9.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_22.addWidget(self.lineEdit_9, 1, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_21)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_22.addWidget(self.label_28, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_21, 7, 0, 3, 2)

        self.groupBox_23 = QGroupBox(self.frame_3)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.gridLayout_25 = QGridLayout(self.groupBox_23)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(-1, 4, -1, 4)
        self.comboBox_4 = QComboBox(self.groupBox_23)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_25.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.groupBox_23)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_25.addWidget(self.pushButton_16, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_23, 10, 0, 1, 2)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_10.addWidget(self.label_2, 1, 0, 1, 2)

        self.groupBox_24 = QGroupBox(self.frame_3)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.gridLayout_26 = QGridLayout(self.groupBox_24)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(-1, 4, -1, 4)
        self.pushButton_26 = QPushButton(self.groupBox_24)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.gridLayout_26.addWidget(self.pushButton_26, 0, 4, 1, 1)

        self.pushButton_25 = QPushButton(self.groupBox_24)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout_26.addWidget(self.pushButton_25, 0, 5, 1, 1)

        self.spinBox_20 = QSpinBox(self.groupBox_24)
        self.spinBox_20.setObjectName(u"spinBox_20")
        self.spinBox_20.setMaximum(60)

        self.gridLayout_26.addWidget(self.spinBox_20, 0, 3, 1, 1)

        self.label_31 = QLabel(self.groupBox_24)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"color: rgb(0, 85, 0);")

        self.gridLayout_26.addWidget(self.label_31, 0, 2, 1, 1)

        self.spinBox_19 = QSpinBox(self.groupBox_24)
        self.spinBox_19.setObjectName(u"spinBox_19")
        self.spinBox_19.setSingleStep(1)

        self.gridLayout_26.addWidget(self.spinBox_19, 0, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_24)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color: rgb(0, 0, 127);")

        self.gridLayout_26.addWidget(self.label_29, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_24, 4, 0, 1, 2)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(320, 180))
        self.label.setMaximumSize(QSize(320, 180))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label.setFrameShape(QFrame.Box)

        self.gridLayout_10.addWidget(self.label, 2, 0, 1, 2)


        self.gridLayout.addWidget(self.frame_3, 0, 6, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Novelti", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Functions", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Yellow Card", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Offside", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Red Card", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Penalty", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Kick Off", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Free Kick", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Extra Time", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Goal", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Live", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Possession", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Team 2", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Corners", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Team 2", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Yellow Cards", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Team 2", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Goals", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Team 2", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Always showing", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Red Cards", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Team 2", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Free Kicks", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Team 2", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Shots on target", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Team 2", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Offsides", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Team 2", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Serves", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Team 2", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Teams", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Intro", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Halftime", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Fulltime", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Abbreviations", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Team 2 ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Video", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Transition Time", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"0.3", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"0.4", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"0.25", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"0.5", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"0.75", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"0.8", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"2", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Substitution", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Team", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Player IN", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Player OUT", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"After Match", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"SPONSORS", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"FINANCE", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"DIGITAL RESOURCES", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"SOFTWARES", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"SPECIAL THANKS", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"FINAL", None))

        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Move to After Match", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Preview Video", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Match time", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Video Here", None))
    # retranslateUi
        # User edits from here
        self.run()
        
    def run(self):
        global SCORE1, SCORE2
        try:
            self.timing = False
            self.time_minutes = 0
            self.time_seconds = 0
            self.timer = QTimer()
            self.timer.start(1000)
            self.timer.timeout.connect(self.update_time)
            self.pushButton_26.clicked.connect(self.toggle_timing)
            self.pushButton_25.clicked.connect(self.reset_timer)
            self.spinBox_19.textChanged.connect(self.edit_time)
            self.spinBox_20.textChanged.connect(self.edit_time)
            
            self.comboBox_3.addItems([self.lineEdit_10.text(),self.lineEdit_11.text()])
            self.lineEdit_10.textChanged.connect(self.update_team)
            self.lineEdit_11.textChanged.connect(self.update_team)
            
            
            self.spinBox.setValue(0)
            self.spinBox_2.setValue(0)
            self.spinBox.textChanged.connect(self.update_team)
            self.spinBox_2.textChanged.connect(self.update_team)
            
            self.comboBox.addItems(CAMLIST)
            self.comboBox.currentTextChanged.connect(self.changeCamera)
            
            # After Match combo box
            self.comboBox_4.currentTextChanged.connect(self.set_after_match_scene)
            # Scenes
            self.pushButton.clicked.connect(self.intro)
            self.pushButton_2.clicked.connect(self.teams)
            self.pushButton_3.clicked.connect(self.live)
            self.pushButton_4.clicked.connect(self.replay)
            self.pushButton_5.clicked.connect(self.half_time)
            self.pushButton_6.clicked.connect(self.full_time)
            self.pushButton_16.clicked.connect(self.after_match)
            
            # Functions
            self.pushButton_7.clicked.connect(self.kick_off)
            self.pushButton_8.clicked.connect(self.offside)
            self.pushButton_9.clicked.connect(self.foul)
            self.pushButton_10.clicked.connect(self.extra_time)
            self.pushButton_11.clicked.connect(self.red_card)
            self.pushButton_12.clicked.connect(self.yellow_card)
            self.pushButton_13.clicked.connect(self.penalty)
            self.pushButton_14.clicked.connect(self.goal)
            
            # Statistics
            self.pushButton_18.clicked.connect(self.shots_on_target)
            self.pushButton_19.clicked.connect(self.free_kicks)
            self.pushButton_17.clicked.connect(self.offsides)
            self.pushButton_24.clicked.connect(self.corners)
            self.pushButton_20.clicked.connect(self.possession)
            self.pushButton_21.clicked.connect(self.red_cards)
            self.pushButton_22.clicked.connect(self.yellow_cards)
            self.pushButton_23.clicked.connect(self.serves)
            
            self.pushButton_15.clicked.connect(self.substitution)
            
            # Extras
            self.pushButton.setCheckable(True)
            self.pushButton_2.setCheckable(True)
            self.pushButton_3.setCheckable(True)
            self.pushButton_4.setCheckable(True)
            self.pushButton_5.setCheckable(True)
            self.pushButton_6.setCheckable(True)
            self.pushButton_16.setCheckable(True)
            
            self.pushButton.setChecked(True)
            self.pushButton_2.setChecked(False)
            self.pushButton_3.setChecked(False)
            self.pushButton_4.setChecked(False)
            self.pushButton_5.setChecked(False)
            self.pushButton_6.setChecked(False)
            self.pushButton_16.setChecked(False)
            
        except Exception as e:
            print(e,':in run')
    
    def reset_timer(self):
        self.time_minutes = 0
        self.time_seconds = 0
        self.spinBox_19.setValue(0)
        self.spinBox_20.setValue(0)
    
    def toggle_timing(self):
        if self.timing:
            self.timing = False
            self.pushButton_26.setText("Continue")
        else:
            self.timing = True
            self.pushButton_26.setText("Pause")
            
    def edit_time(self):
        try:
            seconds = int(self.spinBox_20.text())
        except:
            seconds = 0
        self.time_seconds = seconds
        try:
            minutes = int(self.spinBox_19.text())
        except:
            minutes = 0
        self.time_minutes = minutes
            
               
    def update_time(self):
        if self.timing:
            try:
                seconds = int(self.spinBox_20.text())
            except:
                seconds = 0
            seconds += 1
            if seconds==60:
                self.spinBox_20.setValue(0)
                self.time_seconds = 1
                try:
                    minutes = int(self.spinBox_19.text())
                except:
                    minutes = 0
                minutes += 1
                self.spinBox_19.setValue(minutes)
                self.time_minutes = minutes
            else:
                self.spinBox_20.setValue(seconds)
                self.time_seconds = seconds
                
    def update_team(self):
        global TEAM1,TEAM2,SCORE1,SCORE2
        self.comboBox_3.clear()
        self.comboBox_3.addItems([self.lineEdit_10.text(),self.lineEdit_11.text()])
        TEAM1 = self.lineEdit_10.text()
        TEAM2 = self.lineEdit_11.text()
        SCORE1 = self.spinBox.text()
        SCORE2 = self.spinBox_2.text()
        
    def set_active_button(self,button) :
        self.pushButton.setChecked(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_16.setChecked(False)
        
        button.setChecked(True)
        
    def intro(self):
        duration = float(self.comboBox_2.currentText())
        if not(TRANS_ON) and SCENE!="INTRO":
            Thread(target = trans, args=[duration,"INTRO"], daemon = True).start()
            self.set_active_button(self.pushButton)
            
            
    def teams(self):
        duration = float(self.comboBox_2.currentText())
        if not(TRANS_ON):
            Thread(target = trans, args=[duration,"TEAMS"], daemon = True).start()
            self.set_active_button(self.pushButton_2)
            
    def live(self):
        duration = float(self.comboBox_2.currentText())
        if not(TRANS_ON):
            Thread(target = trans, args=[duration,"LIVE"], daemon = True).start()
            self.set_active_button(self.pushButton_3)
            
    def replay(self):
        global REPLAY_CYCLE
        duration = float(self.comboBox_2.currentText())
        r = []
        rpt = 1
        for frame in REPLAY_FRAMES:
            for i in range(rpt):
                r.append(frame)
        REPLAY_CYCLE = itertools.cycle(r)
        if not(TRANS_ON):
                Thread(target = trans, args=[duration,"REPLAY"], daemon = True).start()
                self.set_active_button(self.pushButton_4)
                
    def half_time(self):
        duration = float(self.comboBox_2.currentText())
        Thread(target = trans, args=[duration,"HALFTIME"], daemon = True).start()
        self.set_active_button(self.pushButton_5)
        # Start timer
        self.timing = False
        self.pushButton_26.setText("Continue")
        self.spinBox_19.setValue(45)
        self.spinBox_20.setValue(0)
        
    def full_time(self):
        duration = float(self.comboBox_2.currentText())
        Thread(target = trans, args=[duration,"FULLTIME"], daemon = True).start()
        self.set_active_button(self.pushButton_6)
    
    def after_match(self):
        global SCENE
        SCENE = "AFTERMATCH"
        self.set_active_button(self.pushButton_16)
    
    def set_after_match_scene(self):
        global AFTERMATCH
        AFTERMATCH = self.comboBox_4.currentText()
        
    def kick_off(self):
        text = self.lineEdit.text()
        self.lineEdit.clear()
        img = FONTS["DIGITAL20"].render(text, True,(255,255,255))
        if len(text)>0:
            msgsurf = IMAGES["msg_kick_off"].copy()
        else:
            msgsurf = pygame.Surface((160,27))
            msgsurf.blit(IMAGES["msg_kick_off"],(0,0))
        msgsurf.blit(img,(9,28))
        MSGLIST.append(msgsurf)
        # Start timer
        self.timing = True
        self.pushButton_26.setText("Pause")
    
    def offside(self):
        text = self.lineEdit_2.text()
        self.lineEdit_2.clear()
        img = FONTS["DIGITAL20"].render(text, True,(76,76,76))
        if len(text)>0:
            msgsurf = IMAGES["msg_offside"].copy()
        else:
            msgsurf = pygame.Surface((160,27))
            msgsurf.blit(IMAGES["msg_offside"],(0,0))
        msgsurf.blit(img,(9,28))
        MSGLIST.append(msgsurf)
    
    def foul(self):
        text = self.lineEdit_3.text()
        self.lineEdit_3.clear()
        img = FONTS["DIGITAL20"].render(text, True,(76,76,76))
        if len(text)>0:
            msgsurf = IMAGES["msg_foul"].copy()
        else:
            msgsurf = pygame.Surface((160,27))
            msgsurf.blit(IMAGES["msg_foul"],(0,0))
        msgsurf.blit(img,(9,28))
        MSGLIST.append(msgsurf)
    
    def extra_time(self):
        text = self.lineEdit_4.text()
        self.lineEdit_4.clear()
        img = FONTS["DIGITAL20"].render(text, True,(255,255,255))
        if len(text)>0:
            msgsurf = IMAGES["msg_extra_time"].copy()
        else:
            msgsurf = pygame.Surface((160,27))
            msgsurf.blit(IMAGES["msg_extra_time"],(0,0))
        msgsurf.blit(img,(9,28))
        MSGLIST.append(msgsurf)
    
    def red_card(self):
        text = self.lineEdit_5.text()
        self.lineEdit_5.clear()
        img = FONTS["DIGITAL20"].render(text, True,(217,0,0))
        if len(text)>0:
            msgsurf = IMAGES["msg_red_card"].copy()
        else:
            msgsurf = pygame.Surface((160,27))
            msgsurf.blit(IMAGES["msg_red_card"],(0,0))
        msgsurf.blit(img,(9,28))
        MSGLIST.append(msgsurf)
    
    def yellow_card(self):
        text = self.lineEdit_6.text()
        self.lineEdit_6.clear()
        img = FONTS["DIGITAL20"].render(text, True,(255,251,19))
        if len(text)>0:
            msgsurf = IMAGES["msg_yellow_card"].copy()
        else:
            msgsurf = pygame.Surface((160,27))
            msgsurf.blit(IMAGES["msg_yellow_card"],(0,0))
        msgsurf.blit(img,(9,28))
        MSGLIST.append(msgsurf)
    
    def penalty(self):
        text = self.lineEdit_7.text()
        self.lineEdit_7.clear()
        img = FONTS["DIGITAL20"].render(text, True,(0,51,217))
        if len(text)>0:
            msgsurf = IMAGES["msg_penalty"].copy()
        else:
            msgsurf = pygame.Surface((160,27))
            msgsurf.blit(IMAGES["msg_penalty"],(0,0))
        msgsurf.blit(img,(9,28))
        MSGLIST.append(msgsurf)
    
    def goal(self):
        text = self.lineEdit_8.text()
        self.lineEdit_8.clear()
        img = FONTS["DIGITAL20"].render(text, True,(255,255,255))
        if len(text)>0:
            msgsurf = IMAGES["msg_goal"].copy()
        else:
            msgsurf = pygame.Surface((160,27))
            msgsurf.blit(IMAGES["msg_goal"],(0,0))
        msgsurf.blit(img,(9,28))
        MSGLIST.append(msgsurf)
        
    def shots_on_target(self):
        text1 = self.spinBox_4.text()
        text2 = self.spinBox_3.text()
        img1 = FONTS["NORMAL21"].render(text1, True,(23,12,231))
        img2 = FONTS["NORMAL21"].render(text2, True,(23,12,231))
        
        msgsurf = IMAGES["stat_shots_on_target"].copy()
        msgsurf.blit(img1,(5,28))
        msgsurf.blit(img2,(155-img2.get_width(),28))
        MSGLIST.append(msgsurf)
    
    def free_kicks(self):
        text1 = self.spinBox_6.text()
        text2 = self.spinBox_5.text()
        img1 = FONTS["NORMAL21"].render(text1, True,(23,12,231))
        img2 = FONTS["NORMAL21"].render(text2, True,(23,12,231))
        
        msgsurf = IMAGES["stat_free_kicks"].copy()
        msgsurf.blit(img1,(5,28))
        msgsurf.blit(img2,(155-img2.get_width(),28))
        MSGLIST.append(msgsurf)
    
    def offsides(self):
        text1 = self.spinBox_8.text()
        text2 = self.spinBox_7.text()
        img1 = FONTS["NORMAL21"].render(text1, True,(23,12,231))
        img2 = FONTS["NORMAL21"].render(text2, True,(23,12,231))
        
        msgsurf = IMAGES["stat_offsides"].copy()
        msgsurf.blit(img1,(5,28))
        msgsurf.blit(img2,(155-img2.get_width(),28))
        MSGLIST.append(msgsurf)

    def corners(self):
        text1 = self.spinBox_10.text()
        text2 = self.spinBox_9.text()
        img1 = FONTS["NORMAL21"].render(text1, True,(23,12,231))
        img2 = FONTS["NORMAL21"].render(text2, True,(23,12,231))
        
        msgsurf = IMAGES["stat_corners"].copy()
        msgsurf.blit(img1,(5,28))
        msgsurf.blit(img2,(155-img2.get_width(),28))
        MSGLIST.append(msgsurf)
    
    def possession(self):
        text1 = self.spinBox_12.text()+"%"
        text2 = self.spinBox_11.text()+"%"
        img1 = FONTS["NORMAL21"].render(text1, True,(23,12,231))
        img2 = FONTS["NORMAL21"].render(text2, True,(23,12,231))
        
        msgsurf = IMAGES["stat_possession"].copy()
        msgsurf.blit(img1,(5,28))
        msgsurf.blit(img2,(155-img2.get_width(),28))
        MSGLIST.append(msgsurf)
    
    def red_cards(self):
        text1 = self.spinBox_14.text()
        text2 = self.spinBox_13.text()
        img1 = FONTS["NORMAL21"].render(text1, True,(23,12,231))
        img2 = FONTS["NORMAL21"].render(text2, True,(23,12,231))
        
        msgsurf = IMAGES["stat_red_cards"].copy()
        msgsurf.blit(img1,(5,28))
        msgsurf.blit(img2,(155-img2.get_width(),28))
        MSGLIST.append(msgsurf)
     
    def yellow_cards(self):
        text1 = self.spinBox_16.text()
        text2 = self.spinBox_15.text()
        img1 = FONTS["NORMAL21"].render(text1, True,(23,12,231))
        img2 = FONTS["NORMAL21"].render(text2, True,(23,12,231))
        
        msgsurf = IMAGES["stat_yellow_cards"].copy()
        msgsurf.blit(img1,(5,28))
        msgsurf.blit(img2,(155-img2.get_width(),28))
        MSGLIST.append(msgsurf)    
    
    def serves(self):
        text1 = self.spinBox_18.text()
        text2 = self.spinBox_17.text()
        img1 = FONTS["NORMAL21"].render(text1, True,(23,12,231))
        img2 = FONTS["NORMAL21"].render(text2, True,(23,12,231))
        
        msgsurf = IMAGES["stat_serves"].copy()
        msgsurf.blit(img1,(5,28))
        msgsurf.blit(img2,(155-img2.get_width(),28))
        MSGLIST.append(msgsurf)
    
    def substitution(self):
        global ANIM_Y
        ANIM_Y = 59
        team = self.comboBox_3.currentText()
        textout = self.lineEdit_12.text()
        textin = self.lineEdit_9.text()
        
        team_img = FONTS["DIGITAL16"].render(team, True,(23,12,231))
        imgout = FONTS["DIGITAL20"].render(textout, True,(244,0,0))
        imgin = FONTS["DIGITAL20"].render(textin, True,(0,149,0))
        
        msgsurf = IMAGES["substitution"].copy()
        msgsurf.blit(team_img,(5,7))
        msgsurf.blit(imgout,(23,31))
        msgsurf.blit(imgin,(23,57))
        MSGLIST.append(msgsurf)
        
    # To choose new camera
    def changeCamera(self):
        global CAMERA_ID, SOURCE_CAM
        try:
            CAMERA_ID = self.comboBox.currentText()
            SOURCE_CAM = pygame.camera.Camera(CAMERA_ID, (WIDTH, HEIGHT), "RGB")
            SOURCE_CAM.start()
        except Exception as e:
            print(e,':in changeCamera')
    
# INITIALIZATIOBS
pygame.init()
pygamecamera.init()

# CONSTANTS
SCENE = "INTRO"
WIDTH = 1280
HEIGHT = 720
FPS = 30
MSGLIST = []
MSGSURF = pygame.Surface((0,0))
TRANS_ON = False
TRANS_X = - WIDTH
PAPER_X = WIDTH
ANIM_ON = False
ANIM_Y = 86
CLOCK = pygame.time.Clock()
CAMLIST = pygame.camera.list_cameras()
CAMERA_ID = CAMLIST[0]

TEAM1 = ""
TEAM2 = ""
SCORE1 = "0"
SCORE2 = "0"
AFTERMATCH = "SPONSORS"
# Camera
SOURCE_CAM = pygame.camera.Camera(CAMERA_ID, (WIDTH, HEIGHT), "RGB")
SOURCE_CAM.start()
print('Available Cameras',CAMLIST)

# Images
IMAGES = {
    "intro_blur" : pygame.image.load("res/intro.png"),
    "intro" : pygame.image.load("res/novelti-live.png"),
    "transition" : pygame.image.load("res/transition.png"),
    "backing" : pygame.image.load("res/paper.png"),
    "cam_error" : pygame.image.load("res/cam-error.png"),
    "match_live" : pygame.image.load("res/novelti-match-live.png"),
    "teams" : pygame.image.load("res/teams.png"),
    "replay" : pygame.image.load("res/novelti-match-replay.png"),
    "half_time" : pygame.image.load("res/half-time.png"),
    "full_time" : pygame.image.load("res/full-time.png"),
    "msg_kick_off" : pygame.image.load("res/msg/kick-off.png"),
    "msg_offside" : pygame.image.load("res/msg/offside.png"),
    "msg_foul" : pygame.image.load("res/msg/foul.png"),
    "msg_extra_time" : pygame.image.load("res/msg/extra-time.png"),
    "msg_red_card" : pygame.image.load("res/msg/red-card.png"),
    "msg_yellow_card" : pygame.image.load("res/msg/yellow-card.png"),
    "msg_penalty" :pygame.image.load("res/msg/penalty.png"),
    "msg_goal" : pygame.image.load("res/msg/goal.png"),
    "stat_shots_on_target" : pygame.image.load("res/msg/shots-on-target.png"),
    "stat_free_kicks" : pygame.image.load("res/msg/free-kicks.png"),
    "stat_offsides" : pygame.image.load("res/msg/offsides.png"),
    "stat_corners" : pygame.image.load("res/msg/corners.png"),
    "stat_possession" : pygame.image.load("res/msg/possession.png"),
    "stat_red_cards" : pygame.image.load("res/msg/red-cards.png"),
    "stat_yellow_cards" : pygame.image.load("res/msg/yellow-cards.png"),
    "stat_serves" : pygame.image.load("res/msg/serves.png"),
    "substitution" : pygame.image.load("res/msg/substitution.png"),
    "sponsors" : pygame.image.load("res/sponsors.png"),
    "softwares" : pygame.image.load("res/softwares.png")
}

# Fonts
FONTS = {
    "DIGITAL16" : pygame.font.Font("res/OCRAEXT.TTF",16),
    "DIGITAL20" : pygame.font.Font("res/OCRAEXT.TTF",20),
    "NORMAL21" : pygame.font.SysFont("Arial",21,True),
    "GOAL" : pygame.font.SysFont("Arial", 44, True)
}

# Replay sequence
REPLAY_FRAMES = [IMAGES["replay"],]

def convert_pygame_to_qt(surface, w,h):
    scaled_img = pygame.transform.smoothscale(surface,(w,h))
    data = scaled_img.get_buffer().raw
    preview_img = QImage(data, 320,180, QImage.Format_RGB32)
    pixmap = QPixmap()
    pixmap.convertFromImage(preview_img)
    return pixmap

def convert_pygame_to_cv2(mysurface, x,y,w,h):
    selected_area = mysurface.subsurface((x,y,w,h))
    img_array = numpy.array(pygame.surfarray.pixels3d(selected_area))
    img_object = numpy.transpose(img_array.reshape((w,h,3)),(1,0,2))
    img_object[:,:,[0,2]] = img_object[:,:,[2,0]]
    return img_object

def trans(duration,scene):
    '''Transition thread'''
    global SCENE, TRANS_ON, TRANS_X, PAPER_X
    TRANS_ON = True
    DIVISOR = 20
    SPEED = 45
    SHIFT = WIDTH/DIVISOR
    # 1st half
    for x in range(DIVISOR):
        TRANS_X += SHIFT
        PAPER_X -= SHIFT
        CLOCK.tick(SPEED)
    # Pause duration
    time.sleep(duration)
    SCENE = scene
    # 2nd half
    for x in range(DIVISOR):
        TRANS_X += SHIFT
        PAPER_X -= SHIFT
        CLOCK.tick(SPEED)
        
    TRANS_X = -WIDTH
    PAPER_X = WIDTH
    TRANS_ON = False
    
    
def anim(msgsurf):
    '''Animation thread'''
    global MSGSURF, ANIM_ON, ANIM_Y
    ANIM_ON = True
    w,h = msgsurf.get_size()
    for y in range(h):
        n = y-h
        MSGSURF = pygame.Surface((w,y))
        MSGSURF.blit(msgsurf, (0,n))
        CLOCK.tick(60)
    time.sleep(3)
    for y in range(h):
        n = 0-y
        MSGSURF = pygame.Surface((w,h-y))
        MSGSURF.blit(msgsurf,(0,n))
        CLOCK.tick(60)
    ANIM_Y = 86
    ANIM_ON = False
    MSGSURF = pygame.Surface((0,0))
        

def main(ui):
    """Main thread"""
    # Virtual Camera
    vcam = pyvirtualcam.Camera(width=WIDTH, height=HEIGHT, fps=FPS)
    print("Virtual Camera created")
    print("Virtual Camera Name: "+vcam.device)
    
    # Main surface
    screen = pygame.Surface((WIDTH,HEIGHT))
    
    # Main thread loop
    while True:
     
        # Get image from camera 
        # for TEAMS, LIVE, HALFTIME, FULLTIME and AFTERMATCH
        if SCENE in ["TEAMS","LIVE","HALFTIME","FULLTIME","AFTERMATCH"]:
            try:
                cam_img = SOURCE_CAM.get_image()
            except:
                cam_img = IMAGES["cam_error"].copy()
            
        # Animation starter
        if len(MSGLIST)>0 and not(ANIM_ON):
            Thread(target=anim, args=[MSGLIST[0],], daemon=True).start()
            MSGLIST.pop(0)
        
        # Intro scene
        if SCENE == "INTRO":
            screen.blit(IMAGES["intro_blur"],(0,0))
            screen.blit(IMAGES["intro"],(0,0))
            
        # Teams scene    
        elif SCENE == "TEAMS":
            screen.blit(cam_img,(0,0))
            screen.blit(IMAGES["teams"],(0,0))
        
        # Live scene
        elif SCENE == "LIVE":
            screen.blit(cam_img,(0,0))
            screen.blit(IMAGES["match_live"],(0,0))
            time_img = FONTS["NORMAL21"].render(str(ui.time_minutes).zfill(2)+":"+str(ui.time_seconds).zfill(2),True,(16,251,254))
            img_team_1 = FONTS["DIGITAL20"].render(TEAM1,True,(36,16,254))
            img_team_2 = FONTS["DIGITAL20"].render(TEAM2,True,(36,16,254))
            img_score_1 = FONTS["NORMAL21"].render(SCORE1,True,(16,251,254))
            img_score_2 = FONTS["NORMAL21"].render(SCORE2,True,(16,251,254))
            
            screen.blit(time_img,(77,33))
            screen.blit(img_team_1,(23,61))
            screen.blit(img_team_2,(176-img_team_2.get_width(),61))
            screen.blit(img_score_1,(69,61))
            screen.blit(img_score_2,(129-img_score_2.get_width(),61))
            screen.blit(MSGSURF,(20,ANIM_Y))
            
            # Preparing video for replay
            # 180 Frames (6 SECONDS)
            REPLAY_FRAMES.append(cam_img.copy())
            if len(REPLAY_FRAMES)>180:
                REPLAY_FRAMES.pop(0)
        
        # Replay scene
        elif SCENE == "REPLAY":
            screen.blit(next(REPLAY_CYCLE),(0,0))
            screen.blit(IMAGES["replay"],(0,0))  
            
        # Half time scene
        elif SCENE == "HALFTIME":
            screen.blit(cam_img,(0,0))
            screen.blit(IMAGES["half_time"],(0,0)) 
            
            img_goal_1 = FONTS["GOAL"].render(SCORE1,True,(43,252,240))
            img_goal_2 = FONTS["GOAL"].render(SCORE2,True,(43,252,240))
            screen.blit(img_goal_1,(566,614))
            screen.blit(img_goal_2,(706-img_goal_2.get_width(),614))
            
        
        # Full time scene
        elif SCENE == "FULLTIME":
            screen.blit(cam_img,(0,0))
            screen.blit(IMAGES["full_time"],(0,0))
            
            img_goal_1 = FONTS["GOAL"].render(SCORE1,True,(43,252,240))
            img_goal_2 = FONTS["GOAL"].render(SCORE2,True,(43,252,240))
            screen.blit(img_goal_1,(566,614))
            screen.blit(img_goal_2,(706-img_goal_2.get_width(),614))
        
        # After Match
        elif SCENE == "AFTERMATCH":
            screen.blit(cam_img,(0,0))
            if AFTERMATCH == "SPONSORS":
                screen.blit(IMAGES["sponsors"],(0,0))
            elif AFTERMATCH == "SOFTWARES":
                screen.blit(IMAGES["softwares"],(0,0))
            
            img_goal_1 = FONTS["GOAL"].render(SCORE1,True,(43,252,240))
            img_goal_2 = FONTS["GOAL"].render(SCORE2,True,(43,252,240))
            screen.blit(img_goal_1,(566,614))
            screen.blit(img_goal_2,(706-img_goal_2.get_width(),614))
                       
        # Transition 
        if TRANS_ON:
            screen.blit(IMAGES["backing"],(PAPER_X,0))
            screen.blit(IMAGES["transition"],(TRANS_X,0))
        
        # Preview pixmap   
        pixmap = convert_pygame_to_qt(screen , 320,180)
        ui.label.setPixmap(pixmap)
        
        # Send screen to virtual camera
        frame = convert_pygame_to_cv2(screen, 0, 0, WIDTH, HEIGHT)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        vcam.send(frame)
        vcam.sleep_until_next_frame()
        
        # 30 FPS
        CLOCK.tick(30)

# Main application        
app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
thread = Thread(target=main, args=[ui,],daemon=True)
thread.start()
app.exec()