# 프로그램 실행시 첫 메인화면
import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'code'))
from userAndPostCtrl import UserAndPostCtrl

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

class UserLogin(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("user_login.ui", self)
        self.buttonBox.accepted.connect(self.courseList)
        self.buttonBox.rejected.connect(self.cancelLogin)

    def courseList(self):
        userCtrl = UserAndPostCtrl()
        Id = self.lineEdit.text()
        pw = self.lineEdit_2.text()

        loginSuccess = userCtrl.checkInfo(Id, pw)

        if loginSuccess:
            QtWidgets.QMessageBox.information(self, 'Success', '로그인 성공.')
            widget.setCurrentIndex(widget.currentIndex()+2)
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 실패. 아이디와 비밀번호를 확인하세요.')
            self.show()

    def cancelLogin(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

class UserRegister(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("user_register.ui", self)
        self.buttonBox.accepted.connect(self.loginLogic)
        self.buttonBox.rejected.connect(self.cancelRegister)

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

    def cancelRegister(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

class CourseList(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("CourseList.ui", self)
        self.toolButton_searchClass.clicked.connect(self.searchClassPage)
        self.toolButton_createCourse.clicked.connect(self.createCoursePage)
        self.pushButton_enterClass.clicked.connect(self.enterCoursePage)

    def searchClassPage(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def createCoursePage(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    def enterCoursePage(self):
        # 사용자가 교사면
        widget.setCurrentIndex(widget.currentIndex()+4)
        # 사용자가 학생이면
        # widget.setCurrentIndex(widget.currentIndex()+5)


class SearchClass(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("SearchClass.ui", self)
        self.pushButton_search.clicked.connect(self.searchLogic)
        self.pushButton_joinClass.clicked.connect(self.joinLogic)

    def searchLogic(self): # 클래스 검색 logic
        pass

    def joinLogic(self): # 클래스 가입 logic
        widget.setCurrentIndex(widget.currentIndex()+2)

class CreateClass(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("create_class.ui", self)
        self.buttonBox.accepted.connect(self.createLogic)
        self.buttonBox.rejected.connect(self.cancelCreate)
    
    def createLogic(self):  # 클래스 생성 logic
        widget.setCurrentIndex(widget.currentIndex()-2)

    def cancelCreate(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

class WriteClasscode(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("write_classcode.ui", self)
        self.buttonBox.accepted.connect(self.successJoin)
        self.buttonBox.rejected.connect(self.cancelJoin)
    
    def successJoin(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    def cancelJoin(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

class HomeworkList_T(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("HomeworkList_teacher.ui", self)
        self.pushButton_registerHomework.clicked.connect(self.registerHWPage)
        self.pushButton_registerHomework.clicked.connect(self.gradeHWPage)
    
    def registerHWPage(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    def gradeHWPage(self):
        widget.setCurrentIndex(widget.currentIndex()+3)

class HomeworkList_S(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("HomeworkList_student.ui", self)
        self.pushButton_checkInfo.clicked.connect(self.checkHWPage)
        self.pushButton_submit.clicked.connect(self.submitHWPage)

    def checkHWPage(self):
        widget.setCurrentIndex(widget.currentIndex()+4)

    def submitHWPage(self):
        widget.setCurrentIndex(widget.currentIndex()+5)

class RegisterHW(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("register_homework.ui", self)
        self.buttonBox.accepted.connect(self.successRegister)
        self.buttonBox.rejected.connect(self.cancelRegister)

    def successRegister(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

    def cancelRegister(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

class GradeHW(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("grade_homework.ui", self)
        self.buttonBox.accepted.connect(self.successGrade)
        self.buttonBox.rejected.connect(self.cancelGrade)

    def successGrade(self):
        widget.setCurrentIndex(widget.currentIndex()-3)

    def cancelGrade(self):
        widget.setCurrentIndex(widget.currentIndex()-3)

class submitHW(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("submit_homework.ui", self)
        self.buttonBox.accepted.connect(self.successSubmit) # type: ignore
        self.buttonBox.rejected.connect(self.cancelSubmit) # type: ignore
        self.pushButton_chooseFile.clicked.connect(self.chooseFile)

    def chooseFile(self): # 파일 선택 logic
        pass

    def successSubmit(self):
        widget.setCurrentIndex(widget.currentIndex()-5)

    def cancelSubmit(self):
        widget.setCurrentIndex(widget.currentIndex()-5)
        
if __name__ == "__main__":
    import sys
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()

    #레이아웃 인스턴스 생성
    mainWindow = MainWindow()
    loginWindow = UserLogin()
    signInWindow = UserRegister()
    courseListWindow = CourseList()
    searchClassWindow = SearchClass()
    createClassWindow = CreateClass()
    writeClasscodeWindow = WriteClasscode()
    HWListTeacherWindow = HomeworkList_T()
    HWListStudentWindow = HomeworkList_S()
    registerHWWindow = RegisterHW()
    gradeHWWindow = GradeHW()

    #Widget 추가
    widget.addWidget(mainWindow)
    widget.addWidget(loginWindow)
    widget.addWidget(signInWindow)
    widget.addWidget(courseListWindow)
    widget.addWidget(searchClassWindow)
    widget.addWidget(createClassWindow)
    widget.addWidget(writeClasscodeWindow)
    widget.addWidget(HWListTeacherWindow)
    widget.addWidget(HWListStudentWindow)
    widget.addWidget(registerHWWindow)
    widget.addWidget(gradeHWWindow)

    #프로그램 화면을 보여주는 코드
    widget.setFixedHeight(400)
    widget.setFixedWidth(500)
    widget.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()