# Form implementation generated from reading ui file 'wifidiscover.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("WIFI Password Discovery")
        MainWindow.resize(400, 624)
        MainWindow.setMinimumSize(QtCore.QSize(400, 0))
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(110, 10, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 0, 0);")
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(12, 61, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inputssid = QtWidgets.QLineEdit(self.centralwidget)
        self.inputssid.setGeometry(QtCore.QRect(52, 60, 231, 21))
        self.inputssid.setObjectName("inputssid")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btngo = QtWidgets.QPushButton(self.centralwidget)
        self.btngo.setGeometry(QtCore.QRect(300, 60, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btngo.setFont(font)
        self.btngo.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.btngo.setObjectName("btngo")
        self.btngo.clicked.connect(self.close)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(11, 91, 371, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.btnclose = QtWidgets.QPushButton(self.centralwidget)
        self.btnclose.setGeometry(QtCore.QRect(300, 590, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnclose.setFont(font)
        self.btnclose.setStyleSheet("background-color: rgb(231, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnclose.setObjectName("btnclose")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 33, 371, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.exibicao = QtWidgets.QLabel(self.centralwidget)
        self.exibicao.setGeometry(QtCore.QRect(10, 110, 371, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exibicao.setFont(font)
        self.exibicao.setAcceptDrops(False)
        self.exibicao.setStyleSheet("color: rgb(255, 0, 0);")
        self.exibicao.setText("")
        self.exibicao.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.exibicao.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.exibicao.setWordWrap(True)
        self.exibicao.setObjectName("exibicao")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 190, 371, 391))
        self.textBrowser.setObjectName("textBrowser")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 167, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Wifi Password Discover"))
        self.label.setText(_translate("MainWindow", "SSID:"))
        self.label_2.setText(_translate("MainWindow", "Security Configurations"))
        self.btngo.setText(_translate("MainWindow", "Go!"))
        self.btnclose.setText(_translate("MainWindow", "Close"))
        self.label_15.setText(_translate("MainWindow", "Result:"))

    def close(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
