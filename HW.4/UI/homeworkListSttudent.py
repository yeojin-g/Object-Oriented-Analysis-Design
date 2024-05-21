# 클래스 입장했을 때 나오는 메인화면 학생버전

from PyQt5 import QtCore, QtGui, QtWidgets


class HomeworkListSudent(object):
    def setupUi(self, MainWindow):
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
        self.pushButton_checkInfo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_checkInfo.setGeometry(QtCore.QRect(140, 310, 113, 32))
        self.pushButton_checkInfo.setObjectName("pushButton_checkInfo")
        # "과제 제출" 푸시 버튼
        self.pushButton_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submit.setGeometry(QtCore.QRect(280, 310, 113, 32))
        self.pushButton_submit.setObjectName("pushButton_submit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "투게더 러닝"))
        self.label_courseName.setText(_translate("MainWindow", "수학"))
        self.label_teacherName.setText(_translate("MainWindow", "홍길동"))
        self.label_homeworkList.setText(_translate("MainWindow", "과제 목록"))
        self.pushButton_checkInfo.setText(_translate("MainWindow", "내용 확인"))
        self.pushButton_submit.setText(_translate("MainWindow", "제출"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = HomeworkListSudent()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
