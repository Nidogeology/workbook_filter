# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 147)
        MainWindow.setStyleSheet("background-color: rgb(17, 17, 17);\n"
"font: 8pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelVariantes = QtWidgets.QLabel(self.centralwidget)
        self.labelVariantes.setObjectName("labelVariantes")
        self.gridLayout.addWidget(self.labelVariantes, 3, 1, 1, 3)
        self.btnSetColumn = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetColumn.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.btnSetColumn.setObjectName("btnSetColumn")
        self.gridLayout.addWidget(self.btnSetColumn, 1, 3, 1, 1)
        self.btnOpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFile.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.gridLayout.addWidget(self.btnOpenFile, 0, 3, 1, 1)
        self.btnFilter = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilter.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"border-color: rgb(255, 255, 255);")
        self.btnFilter.setObjectName("btnFilter")
        self.gridLayout.addWidget(self.btnFilter, 4, 3, 1, 1)
        self.labelTermo = QtWidgets.QLabel(self.centralwidget)
        self.labelTermo.setObjectName("labelTermo")
        self.gridLayout.addWidget(self.labelTermo, 3, 0, 1, 1)
        self.inputVariantes = QtWidgets.QLineEdit(self.centralwidget)
        self.inputVariantes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputVariantes.setObjectName("inputVariantes")
        self.gridLayout.addWidget(self.inputVariantes, 4, 1, 1, 2)
        self.inputChooseFile = QtWidgets.QLineEdit(self.centralwidget)
        self.inputChooseFile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputChooseFile.setObjectName("inputChooseFile")
        self.gridLayout.addWidget(self.inputChooseFile, 0, 1, 1, 2)
        self.inputTermo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTermo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputTermo.setObjectName("inputTermo")
        self.gridLayout.addWidget(self.inputTermo, 4, 0, 1, 1)
        self.labelColuna = QtWidgets.QLabel(self.centralwidget)
        self.labelColuna.setObjectName("labelColuna")
        self.gridLayout.addWidget(self.labelColuna, 1, 0, 1, 1)
        self.labelOpen = QtWidgets.QLabel(self.centralwidget)
        self.labelOpen.setObjectName("labelOpen")
        self.gridLayout.addWidget(self.labelOpen, 0, 0, 1, 1)
        self.inputColuna = QtWidgets.QLineEdit(self.centralwidget)
        self.inputColuna.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputColuna.setObjectName("inputColuna")
        self.gridLayout.addWidget(self.inputColuna, 1, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 8pt \"Comic Sans MS\";\n"
"color: rgb(33, 33, 33);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 3, 1, 1)
        self.btnSaveFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveFile.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.btnSaveFile.setObjectName("btnSaveFile")
        self.gridLayout.addWidget(self.btnSaveFile, 5, 2, 1, 1)
        self.btnRest = QtWidgets.QPushButton(self.centralwidget)
        self.btnRest.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.btnRest.setObjectName("btnRest")
        self.gridLayout.addWidget(self.btnRest, 5, 1, 1, 1)
        self.btnFilter.raise_()
        self.labelTermo.raise_()
        self.inputTermo.raise_()
        self.inputVariantes.raise_()
        self.labelVariantes.raise_()
        self.inputChooseFile.raise_()
        self.labelOpen.raise_()
        self.labelColuna.raise_()
        self.inputColuna.raise_()
        self.btnSetColumn.raise_()
        self.btnOpenFile.raise_()
        self.label.raise_()
        self.btnSaveFile.raise_()
        self.btnRest.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inputChooseFile, self.btnOpenFile)
        MainWindow.setTabOrder(self.btnOpenFile, self.inputColuna)
        MainWindow.setTabOrder(self.inputColuna, self.btnSetColumn)
        MainWindow.setTabOrder(self.btnSetColumn, self.inputTermo)
        MainWindow.setTabOrder(self.inputTermo, self.inputVariantes)
        MainWindow.setTabOrder(self.inputVariantes, self.btnFilter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Filtrar planilha"))
        self.labelVariantes.setText(_translate("MainWindow", "Inserir variações entre vírgulas (ex: email, e mail) "))
        self.btnSetColumn.setText(_translate("MainWindow", "Definir coluna"))
        self.btnOpenFile.setText(_translate("MainWindow", "Abrir"))
        self.btnFilter.setText(_translate("MainWindow", "Filtrar"))
        self.labelTermo.setText(_translate("MainWindow", "Inserir termo (ex: e-mail)"))
        self.labelColuna.setText(_translate("MainWindow", "Coluna:"))
        self.labelOpen.setText(_translate("MainWindow", "Escolher arquivo:"))
        self.label.setText(_translate("MainWindow", "by: @nidogeology"))
        self.btnSaveFile.setText(_translate("MainWindow", "Salvar"))
        self.btnRest.setText(_translate("MainWindow", "Gerar restante"))
