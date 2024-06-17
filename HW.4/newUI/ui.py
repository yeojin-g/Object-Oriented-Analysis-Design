# 프로그램 실행시 첫 메인화면
import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QListWidget
from PyQt5.uic import loadUi
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'newCode'))
from userCtrl import UserCtrl
from user import User
from classCtrl import ClassCtrl

currentUserInfo = []
currentUser = User(0, 0, 0, 0)

class MainWindow(QDialog): # main창(first page)
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("FirstPage.ui", self)
        self.toolButton_login.clicked.connect(self.loginPage)
        self.toolButton_register.clicked.connect(self.signInPage)

    def loginPage(self):
        widget.setCurrentWidget(loginWindow)

    def signInPage(self):
        widget.setCurrentWidget(signInWindow)

class UserLogin(QDialog): # Login창
    def __init__(self) :
        super().__init__()
        loadUi("user_login.ui", self)
        self.buttonBox.accepted.connect(self.courseList)
        self.buttonBox.rejected.connect(self.cancelLogin)

    def courseList(self):
        userCtrl = UserCtrl()
        Id = self.lineEdit.text()
        pw = self.lineEdit_2.text()

        loginSuccess = userCtrl.Login(Id, pw)
        currentUser = userCtrl.Login(Id, pw)

        if loginSuccess:
            QtWidgets.QMessageBox.information(self, 'Success', '로그인 성공.')
            widget.setCurrentWidget(courseListWindow)
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', '로그인 실패. 아이디와 비밀번호를 확인하세요.')
            self.show()

    def cancelLogin(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

class UserRegister(QDialog): # SignIn창
    def __init__(self) :
        super().__init__()
        loadUi("user_register.ui", self)
        self.buttonBox.accepted.connect(self.loginLogic)
        self.buttonBox.rejected.connect(self.cancelRegister)

    def loginLogic(self): #Login logic
        global currentUserInfo
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
        
        userCrtl = UserCtrl() # ctrl 객체 생성
        currentUserInfo = [roleNum, name, Id, pw, email]
        isSuccess = userCrtl.signIn(roleNum, name, Id, pw, email) # signIn 수행
        print(currentUserInfo)
        
        if isSuccess:
            widget.setCurrentIndex(widget.currentIndex()-2)

    def cancelRegister(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

class CourseList(QDialog): # 현재 user가 속한 CourseList 보여주는 창
    def __init__(self) :
        super().__init__()
        loadUi("CourseList.ui", self)
        self.toolButton_searchClass.clicked.connect(self.searchClassPage)
        self.toolButton_createCourse.clicked.connect(self.createCoursePage)
        self.pushButton_enterClass.clicked.connect(self.enterClassPage)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setHorizontalHeaderLabels(["클래스 이름", "교사 이름"])
        for r in range(self.tableWidget.rowCount()):
            index = 0
            for c in range(self.tableWidget.columnCount()):
                # 테이블위젯아이템 생성
                item = QTableWidgetItem()
                # 아이템에 데이터 삽입
                item.setText(currentUser.getClassList()[getClassInfo()[index]])
                index += 2
                # 아이템을 테이블에 세팅
                self.tableWidget.setItem(r, c, item)
                
        self.tableWidget.currentCellChanged.connect(self.currentcellchanged_event)
        widget.update()
        widget.currentChanged.connect(self.widgetUpdate)

    def widgetUpdate(self):
        widget.update()

    def currentcellchanged_event(self, row, col, pre_row, pre_col):
        current_data = self.tableWidget.item(row, col) # 현재 선택 셀 값
        pre_data = self.tableWidget.item(pre_row, pre_col) # 이전 선택 셀 값
        if pre_data is not None:
            print("이전 선택 셀 값 : ", pre_data.text())
        else:
            print("이전 선택 셀 값 : 없음")

        print("현재 선택 셀 값 : ", current_data.text())

    def searchClassPage(self): # 클래스 검색 
        if currentUserInfo[0] == 0:
            QtWidgets.QMessageBox.warning(self, 'Error', '사용할 수 없는 기능입니다.')
            self.show()
        else:    
            widget.setCurrentIndex(widget.currentIndex()+1)

    def createCoursePage(self): # 클래스 생성
        if currentUserInfo[0] == 0:
            widget.setCurrentIndex(widget.currentIndex()+2)
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', '사용할 수 없는 기능입니다.')
            self.show()

    def enterClassPage(self): # 클래스 입장
        # 사용자가 교사면
        if currentUserInfo[0] == 0:
            widget.setCurrentWidget(HWListTeacherWindow)
        # 사용자가 학생이면
        elif currentUserInfo[0] == 1:
            widget.setCurrentWidget(HWListStudentWindow)
        # 사용자가 부모이면
        elif currentUserInfo[0] == 2:
            widget.setCurrentWidget(HWListParentWindow)


class SearchClass(QDialog): # 클래스 검색
    def __init__(self) :
        super().__init__()
        loadUi("SearchClass.ui", self)
        self.pushButton_search.clicked.connect(self.searchLogic)
        self.pushButton_joinClass.clicked.connect(self.joinLogic)

    def searchLogic(self): # 클래스 검색 logic
        className = self.lineEdit.text()

    def joinLogic(self): # 클래스 가입 logic
        widget.setCurrentIndex(widget.currentIndex()+2)

class CreateClass(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("create_class.ui", self)
        self.buttonBox.accepted.connect(self.createLogic)
        self.buttonBox.rejected.connect(self.cancelCreate)
    
    def createLogic(self):  # 클래스 생성 logic
        global currentUserInfo
        
        classCtrl = ClassCtrl()
        name = self.lineEdit_className.text()
        code = self.lineEdit_classCode.text()
        teacherId = currentUserInfo[2]
        classCtrl.makeClass(name, code, teacherId)
        widget.setCurrentIndex(widget.currentIndex()-2)
        widget.currentChanged.connect(self.widgetUpdate)

    def widgetUpdate(self):
        widget.update()

    def cancelCreate(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

class WriteClasscode(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("write_classcode.ui", self)
        self.buttonBox.accepted.connect(self.successJoin)
        self.buttonBox.rejected.connect(self.cancelJoin)

    def checkClassCode(self, code) :
        classCode = self.lineEdit_classCode.text()
    
    def successJoin(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    def cancelJoin(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

class HomeworkList_T(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("HomeworkList_teacher.ui", self)
        self.pushButton_registerHomework.clicked.connect(self.registerHWPage)
        self.pushButton_gradeHomework.clicked.connect(self.gradeHWPage)

        self.listWidget.insertItem(i, currentUser.getClassList.getHomeworkList()[0])
    
    def registerHWPage(self):
        widget.setCurrentWidget(registerHWWindow)

    def gradeHWPage(self):
        widget.setCurrentWidget(gradeHWWindow)

class HomeworkList_S(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("HomeworkList_student.ui", self)
        self.pushButton_checkInfo.clicked.connect(self.checkHWPage)
        self.pushButton_submit.clicked.connect(self.submitHWPage)

    def checkHWPage(self):
        widget.setCurrentWidget(checkHWWindow)

    def submitHWPage(self):
        widget.setCurrentWidget(submitHWWindow)

class RegisterHW(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("register_homework.ui", self)
        self.buttonBox.accepted.connect(self.successRegister)
        self.buttonBox.rejected.connect(self.cancelRegister)

    def successRegister(self):
        widget.setCurrentWidget(HWListTeacherWindow)
    def cancelRegister(self):
        widget.setCurrentWidget(HWListTeacherWindow)

class GradeHW(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("grade_homework.ui", self)
        self.buttonBox.accepted.connect(self.successGrade)
        self.buttonBox.rejected.connect(self.cancelGrade)

    def successGrade(self):
        widget.setCurrentWidget(HWListTeacherWindow)

    def cancelGrade(self):
        widget.setCurrentWidget(HWListTeacherWindow)


class SubmitHW(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("submit_homework.ui", self)
        self.buttonBox.accepted.connect(self.successSubmit) # type: ignore
        self.buttonBox.rejected.connect(self.cancelSubmit) # type: ignore
        self.pushButton_chooseFile.clicked.connect(self.chooseFile)

    def chooseFile(self): # 파일 선택 logic
        pass

    def successSubmit(self):
        widget.setCurrentWidget(HWListStudentWindow)

    def cancelSubmit(self):
        widget.setCurrentWidget(HWListStudentWindow)

class HomeworkList_P(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("HomeworkList_parent.ui", self)
        self.pushButton_checkInfo.clicked.connect(self.checkHWPage)

    def checkHWPage(self):
        widget.setCurrentWidget(checkHWWindow)

class CheckHW(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi("checkHomework.ui", self)
        self.pushButton_downloadSubmitHW.clicked.connect(self.download)

    def download(self): # 제출 과제 다운로드 logic
        pass
        
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
    submitHWWindow = SubmitHW()
    HWListParentWindow = HomeworkList_P()
    checkHWWindow = CheckHW()

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
    widget.addWidget(submitHWWindow)
    widget.addWidget(HWListParentWindow)
    widget.addWidget(checkHWWindow)

    #프로그램 화면을 보여주는 코드
    widget.setFixedHeight(400)
    widget.setFixedWidth(500)
    widget.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()