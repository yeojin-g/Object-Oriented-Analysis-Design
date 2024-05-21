# 클래스 입장시 나오는 메인화면 교사버전


from PyQt5 import QtCore, QtGui, QtWidgets


class HomeworkListTeacher(object):
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
        
        # "과제 등록" 푸시버튼
        self.pushButton_uploadHomework = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uploadHomework.setGeometry(QtCore.QRect(140, 310, 113, 32))
        self.pushButton_uploadHomework.setObjectName("pushButton_uploadHomework")

        # "과제 채점" 푸시버튼
        self.pushButton_grade = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_grade.setGeometry(QtCore.QRect(280, 310, 113, 32))
        self.pushButton_grade.setObjectName("pushButton_grade")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_courseName.setText(_translate("MainWindow", "수학"))
        self.label_teacherName.setText(_translate("MainWindow", "홍길동"))
        self.label_homeworkList.setText(_translate("MainWindow", "과제 목록"))
        self.pushButton_uploadHomework.setText(_translate("MainWindow", "등록"))
        self.pushButton_grade.setText(_translate("MainWindow", "채점"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = HomeworkListTeacher()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
