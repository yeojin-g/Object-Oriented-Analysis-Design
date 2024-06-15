# 프로그램 실행시 첫 메인화면
import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("FirstPage.ui", self)
        self.toolButton_login.clicked.connect(self.loginPage)
        self.toolButton_register.clicked.connect(self.signInPage)

    def loginPage(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signInPage(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

class CourseList(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("CourseList", self)

class UserLogin(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("user_login.ui", self)

    def courseList(self):
        userCtrl = UserAndPostCtrl()
        Id = self.lineEdit.text()
        pw = self.lineEdit_2.text()

        loginSuccess = userCtrl.checkInfo(Id, pw)

        if loginSuccess:
            QtWidgets.QMessageBox.information(self.curPage, 'Success', '로그인 성공.')
            widget.setCurrentIndex(widget.currentIndex()+2)  
        else:
            QtWidgets.QMessageBox.warning(self.curPage, 'Error', '로그인 실패. 아이디와 비밀번호를 확인하세요.')

    def cancelLogin(self):
        self.curPage.reject()
        self.main.show()

class UserRegister(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("user_register.ui", self)

    def loginLogic(self): #Login logic
        Id = self.lineEdit.text()
        pw = self.lineEdit_2.text()
        name = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        roleNum = -1
        
        #역할 선택에 맞는 roleNum 설정
        if self.radioButton.isChecked():
            roleNum = 0
        elif self.radioButton_2.isChecked():
            roleNum = 1
        elif self.radioButton_3.isChecked():
            roleNum = 2
        
        userCrtl = UserAndPostCtrl() # ctrl 객체 생성
        isSuccess = userCrtl.signIn(roleNum, name, Id, pw, email) # signIn 수행
        
        if isSuccess:
            widget.setCurrentIndex(widget.currentIndex()-2)

        
if __name__ == "__main__":
    import sys
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()

    #레이아웃 인스턴스 생성
    mainWindow = MainWindow()
    loginwindow = UserLogin()
    SignInwindow = User

    #Widget 추가
    widget.addWidget(mainWindow)
    widget.addWidget(loginwindow)

    #프로그램 화면을 보여주는 코드
    widget.setFixedHeight(400)
    widget.setFixedWidth(600)
    widget.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()