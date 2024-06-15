from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtTest
import math

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        uic.loadUi('mainUI.ui', self)
        self.setWindowTitle('Group 2: Permutation GUI..')
        self.show()
        
        ## VARIABLES
        self.redButton = 'background-color: #ee2e31;color: black;font: 87 7pt "Arial Black";'
        self.normalButton = 'background-color: #f4c095;color: black;font: 87 7pt "Arial Black";'
        self.isInCombi = True
        self.isInCombiWithRepeat = False
        self.isInPermuWithReplacement = False
        self.isInPermu = False
        # CLICK HANDLER
        self.pushButton.clicked.connect(self.combiFunction)
        self.pushButton_2.clicked.connect(self.combiWithRepeatFunction)
        self.pushButton_3.clicked.connect(self.permuWithReplacementFunction)
        self.pushButton_4.clicked.connect(self.permuFunction)
        
        ## EVENT HANDLER
        self.textEdit.textChanged.connect(self.caculateCombi)
        self.textEdit_2.textChanged.connect(self.caculateCombi)
        self.textEdit_4.textChanged.connect(self.calculateCombiWithRepeat)
        self.textEdit_3.textChanged.connect(self.calculateCombiWithRepeat)
        self.textEdit_19.textChanged.connect(self.calculatePermuWithReplacement)
        self.textEdit_20.textChanged.connect(self.calculatePermuWithReplacement)
        self.textEdit_6.textChanged.connect(self.calculatePermu)
        self.textEdit_5.textChanged.connect(self.calculatePermu)
        
    def combiFunction(self):
        self.pushButton.setStyleSheet(self.redButton)
        self.pushButton_2.setStyleSheet(self.normalButton)
        self.pushButton_3.setStyleSheet(self.normalButton)
        self.pushButton_4.setStyleSheet(self.normalButton)
        self.stackedWidget.setCurrentIndex(0)
        self.isInCombi = True
        self.isInCombiWithRepeat = False
        self.isInPermuWithReplacement = False
        self.isInPermu = False
        
    def caculateCombi(self):
        N = self.textEdit.toPlainText()
        R = self.textEdit_2.toPlainText()
        if R.isdigit() and N.isdigit():
            n = int(N)
            r = int(R)
            if n > r:
                self.label_4.setText(str(n))
                self.label_6.setText(str(r))
                self.label_9.setText(str(math.factorial(n)))
                self.label_10.setText(str(math.factorial(r)))
                self.label_12.setText(str(f'({math.factorial(n-r)})'))
                self.label_16.setText(str((math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))))
    def calculateCombiWithRepeat(self):
        N = self.textEdit_4.toPlainText()
        R = self.textEdit_3.toPlainText()
        if R.isdigit() and N.isdigit():
            n = int(N)
            r = int(R)
            if n > r:
                self.label_20.setText(str(n))
                self.label_25.setText(str(r))
                self.label_37.setText(str(math.factorial( r + n - 1)))
                self.label_19.setText(str(math.factorial(r)))
                self.label_22.setText(str(f'( {math.factorial(n - 1)} )'))
                self.label_31.setText(str((math.factorial(r + n -1))/(math.factorial(r)*math.factorial(n-1))))
    def calculatePermu(self):
        N = self.textEdit_6.toPlainText()
        R = self.textEdit_5.toPlainText()
        if R.isdigit() and N.isdigit():
            n = int(N)
            r = int(R)
            if n > r:
                self.label_50.setText(str(n))
                self.label_46.setText(str(r))
                self.label_43.setText(str(math.factorial(n)))
                self.label_45.setText(str(math.factorial(n - r)))
                self.label_58.setText(str((math.factorial(n))/(math.factorial(n - r))))
    def calculatePermuWithReplacement(self):
        N = self.textEdit_19.toPlainText()
        R = self.textEdit_20.toPlainText()
        if R.isdigit() and N.isdigit():
            n = int(N)
            r = int(R)
            if n > r:
                self.label_169.setText(str(n))
                self.label_158.setText(str(r))
                self.label_160.setText(str(n**r))
                self.label_165.setText(str(n**r))

        
    def combiWithRepeatFunction(self):
        self.pushButton.setStyleSheet(self.normalButton)
        self.pushButton_2.setStyleSheet(self.redButton)
        self.pushButton_3.setStyleSheet(self.normalButton)
        self.pushButton_4.setStyleSheet(self.normalButton)
        self.stackedWidget.setCurrentIndex(1)
        self.isInCombi = False
        self.isInCombiWithRepeat = True
        self.isInPermuWithReplacement = False
        self.isInPermu = False
    def permuWithReplacementFunction(self):
        self.pushButton.setStyleSheet(self.normalButton)
        self.pushButton_2.setStyleSheet(self.normalButton)
        self.pushButton_3.setStyleSheet(self.redButton)
        self.pushButton_4.setStyleSheet(self.normalButton)
        self.stackedWidget.setCurrentIndex(2)
    def permuFunction(self):
        self.pushButton.setStyleSheet(self.normalButton)
        self.pushButton_2.setStyleSheet(self.normalButton)
        self.pushButton_3.setStyleSheet(self.normalButton)
        self.pushButton_4.setStyleSheet(self.redButton)
        self.stackedWidget.setCurrentIndex(3)
    
    
    
        
        
app = QApplication([])
window = mainWindow()
app.exec_()
