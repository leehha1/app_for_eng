import pandas as pd
import sqlite3 as sq
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.StartButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.StartButton.setObjectName("StartButton")

        self.gridLayout.addWidget(self.StartButton, 3, 1, 1, 1)

        self.labelNumberOfAns = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelNumberOfAns.setObjectName("labelNumberOfAns")

        self.gridLayout.addWidget(self.labelNumberOfAns, 0, 2, 1, 1)
        self.labelFromLang = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelFromLang.setObjectName("labelFromLang")
        self.gridLayout.addWidget(self.labelFromLang, 0, 0, 1, 1)
        self.spinBoxNumbOfAns = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxNumbOfAns.setMinimum(2)
        self.spinBoxNumbOfAns.setMaximum(4)
        self.spinBoxNumbOfAns.setObjectName("spinBoxNumbOfAns")
        self.gridLayout.addWidget(self.spinBoxNumbOfAns, 1, 2, 1, 1)
        self.labelIntoLang = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelIntoLang.setObjectName("labelIntoLang")
        self.gridLayout.addWidget(self.labelIntoLang, 0, 1, 1, 1)
        self.labelScore = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelScore.setObjectName("labelScore")
        self.gridLayout.addWidget(self.labelScore, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.comboBoxFromLang = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBoxFromLang.setObjectName("comboBoxFromLang")
        self.comboBoxFromLang.addItem("")
        self.comboBoxFromLang.addItem("")
        self.gridLayout.addWidget(self.comboBoxFromLang, 1, 0, 1, 1)
        self.comboBoxIntoLang = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBoxIntoLang.setObjectName("comboBoxIntoLang")
        self.comboBoxIntoLang.addItem("")
        self.comboBoxIntoLang.addItem("")
        self.gridLayout.addWidget(self.comboBoxIntoLang, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 190, 801, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.labelFromWord = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelFromWord.setFont(font)
        self.labelFromWord.setObjectName("labelFromWord")
        self.horizontalLayout.addWidget(self.labelFromWord)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 320, 801, 203))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonAns1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonAns1.setFont(font)
        self.pushButtonAns1.setObjectName("pushButtonAns1")
        self.gridLayout_2.addWidget(self.pushButtonAns1, 0, 0, 1, 1)
        self.pushButtonAns3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonAns3.setFont(font)
        self.pushButtonAns3.setObjectName("pushButtonAns3")
        self.gridLayout_2.addWidget(self.pushButtonAns3, 2, 0, 1, 1)
        self.pushButtonAns2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonAns2.setFont(font)
        self.pushButtonAns2.setObjectName("pushButtonAns2")
        self.gridLayout_2.addWidget(self.pushButtonAns2, 1, 0, 1, 1)
        self.pushButtonAns4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonAns4.setFont(font)
        self.pushButtonAns4.setObjectName("pushButtonAns4")
        self.gridLayout_2.addWidget(self.pushButtonAns4, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translator"))
        
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.labelNumberOfAns.setText(_translate("MainWindow", "Number of answer options"))
        self.labelFromLang.setText(_translate("MainWindow", "From language"))
        self.labelIntoLang.setText(_translate("MainWindow", "Into language"))
        self.labelScore.setText(_translate("MainWindow", "Score:"))

        self.comboBoxFromLang.setCurrentText(_translate("MainWindow", "text1"))
        self.comboBoxFromLang.setItemText(0, _translate("MainWindow", "text1"))
        self.comboBoxFromLang.setItemText(1, _translate("MainWindow", "text2"))

        self.comboBoxIntoLang.setCurrentText(_translate("MainWindow", "text1"))
        self.comboBoxIntoLang.setItemText(0, _translate("MainWindow", "text1"))
        self.comboBoxIntoLang.setItemText(1, _translate("MainWindow", "text2"))

        self.labelFromWord.setText(_translate("MainWindow", "TextLabel"))

        self.pushButtonAns1.setText(_translate("MainWindow", "PushButton"))
        self.pushButtonAns3.setText(_translate("MainWindow", "PushButton"))
        self.pushButtonAns2.setText(_translate("MainWindow", "PushButton"))
        self.pushButtonAns4.setText(_translate("MainWindow", "PushButton"))



def createTableWords(cur):
    query = """CREATE TABLE IF NOT EXISTS words (
        word_id INTEGER PRIMARY KEY AUTOINCREMENT,
        eng TEXT NOT NULL,
        ru TEXT,
        ua TEXT,
        transcr TEXT
        );
        """
    cur.execute(query)

def returnRandomWords(number, cur):
    
    query = f"SELECT * FROM words ORDER BY RANDOM() LIMIT {number};"
    cur.execute(query)
    
    return cur.fetchall()


if __name__ == "__main__":
    numberRandomWords = 4

    con = None
    try:
        con = sq.connect("translation.db")
        cur = con.cursor()

        createTableWords(cur)
        # returnRandomWords(numberRandomWords, cur)

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


    except sq.Error as e:
        if con: con.rollback()
        print("Request execution error")
    
    finally:
        if con: con.close()


    



# path = "D:/python/app_for_eng/words.csv"
# df = pd.read_csv(path)
# print(df.head())