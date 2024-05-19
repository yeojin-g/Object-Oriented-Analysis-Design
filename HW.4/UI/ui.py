import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Together Learnig') # page title 넣기
        self.setWindowIcon(QIcon('icon.png')) # icon 넣기
        self.setGeometry(500, 150, 1000, 700)
        self.showBoxLayout()
        self.show()
    
    def showBoxLayout(self):
        # input Id, pw
        inputId = QLineEdit(self)
        inputPw = QLineEdit(self)
        
        label1 = QLabel('Login', self)
        label1.setAlignment(Qt.AlignCenter)
        
        btn1 = QPushButton('완료', self)
        
        hboxB = QHBoxLayout()
        hboxB.addStretch(1)
        hboxB.addWidget(btn1)
        hboxB.addStretch(1)
        
        vbox1 = QVBoxLayout()
        vbox1.addStretch(2)
        vbox1.addWidget(label1)
        vbox1.addWidget(inputId)
        vbox1.addWidget(inputPw)
        vbox1.addLayout(hboxB)
        vbox1.addStretch(2)
        
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addLayout(vbox1, 3)
        hbox1.addStretch(1)

        self.setLayout(hbox1)
        
    

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Login()
   sys.exit(app.exec_())