# 클래스 입장했을 때 나오는 메인화면 학생버전

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from submitHomework import SubmitHomework
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'code'))
from course import Course

class HomeworkListSudent(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 403)

        # icon 넣기
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # "클래스 이름" 라벨
        self.label_courseName = QtWidgets.QLabel(self.centralwidget)
        self.label_courseName.setGeometry(QtCore.QRect(140, 30, 60, 16))
        self.label_courseName.setObjectName("label_courseName")

        # "교사 이름" 라벨
        self.label_teacherName = QtWidgets.QLabel(self.centralwidget)
        self.label_teacherName.setGeometry(QtCore.QRect(210, 30, 60, 16))
        self.label_teacherName.setObjectName("label_teacherName")
        # "과제 목록" 라벨
        self.label_homeworkList = QtWidgets.QLabel(self.centralwidget)
        self.label_homeworkList.setGeometry(QtCore.QRect(140, 70, 60, 16))
        self.label_homeworkList.setObjectName("label_homeworkList")
        # 과제 목록용 listWidget
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(140, 100, 256, 192))
        self.listWidget.setObjectName("listWidget")
        # "내용 확인" 푸시 버튼
        self.pushButton_checkHomework = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_checkHomework.setGeometry(QtCore.QRect(140, 310, 113, 32))
        self.pushButton_checkHomework.setObjectName("pushButton_checkInfo")
        # "과제 제출" 푸시 버튼
        self.pushButton_submitHomework = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submitHomework.setGeometry(QtCore.QRect(280, 310, 113, 32))
        self.pushButton_submitHomework.setObjectName("pushButton_submit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.connectButton()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "투게더 러닝"))
        self.label_courseName.setText(_translate("MainWindow", "수학"))
        self.label_teacherName.setText(_translate("MainWindow", "홍길동"))
        self.label_homeworkList.setText(_translate("MainWindow", "과제 목록"))
        self.pushButton_checkHomework.setText(_translate("MainWindow", "내용 확인"))
        self.pushButton_submitHomework.setText(_translate("MainWindow", "제출"))

    def connectButton(self):    # 버튼과 전환함수 연결
        self.pushButton_checkHomework.clicked.connect(self.checkHomework)
        self.pushButton_submitHomework.clicked.connect(self.submitHomework)

    def checkHomework(self): # 과제 내용 확인 페이지로 전환하는 함수
        pass

    def showList(self): # 과제 목록 보여주는 함수
        pass

    def submitHomework(self): # 과제 제출 페이지로 전환하는 함수
        self.MainWindow.hide()

        newDialog = QtWidgets.QDialog()
        nextPage = SubmitHomework()
        nextPage.setupUi(newDialog)
        newDialog.exec_()
        self.MainWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = HomeworkListSudent()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
