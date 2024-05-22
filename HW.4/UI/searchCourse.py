# 클래스 검색을 위한 메인화면
# courseList에서 클래스 검색 툴버튼을 누르면 이 화면으로 이동
# 클래스 검색 입력창에 클래스 이름 입력 후 검색 버튼을 누르면 밑의 tableWidget에 [클래스 이름, 교사 이름] 형태로 클래스 목록이 나오도록 할 예정
# 목록에서 클래스를 선택해 클래스 가입 툴버튼을 누르면 가입용 팝업창이 나오도록 할 예정  
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'code'))
from courseCtrl import CourseCtrl
from course import Course


class SearchCourse(object):
    def setupUi(self, MainWindow):
        self.Mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 403)

        # icon 넣기
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 검색한 클래스 목록용 tableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 161, 291, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        # "클래스 가입" 푸시버튼
        self.pushButton_joinClass = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_joinClass.setGeometry(QtCore.QRect(190, 310, 113, 32))
        self.pushButton_joinClass.setObjectName("pushButton_joinClass")

        # "클래스 목록" 라벨
        self.label_classList = QtWidgets.QLabel(self.centralwidget)
        self.label_classList.setGeometry(QtCore.QRect(210, 130, 60, 16))
        self.label_classList.setObjectName("label_classList")

        # 검색용 입력창
        self.lineEdit_searchClass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_searchClass.setGeometry(QtCore.QRect(110, 90, 211, 21))
        self.lineEdit_searchClass.setObjectName("lineEdit_searchClass")

        # 검색용 푸시버튼
        self.pushButton_searchClass = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_searchClass.setGeometry(QtCore.QRect(330, 86, 65, 32))
        self.pushButton_searchClass.setObjectName("pushButton_searchClass")
        self.pushButton_searchClass.clicked.connect(self.findCourse)

        # "클래스 검색" 라벨
        self.label_searchClass = QtWidgets.QLabel(self.centralwidget)
        self.label_searchClass.setGeometry(QtCore.QRect(210, 50, 60, 16))
        self.label_searchClass.setObjectName("label_searchClass")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "클래스 검색"))
        self.pushButton_joinClass.setText(_translate("MainWindow", "클래스 가입"))
        self.label_classList.setText(_translate("MainWindow", "클래스 목록"))
        self.pushButton_searchClass.setText(_translate("MainWindow", "검색"))
        self.label_searchClass.setText(_translate("MainWindow", "클래스 검색"))

    def findCourse(self):
        self.courseName = self.lineEdit_searchClass.text()
        self.courseCtrl = CourseCtrl()
        self.searchResult = self.courseCtrl.searchCourse(self.courseName)
        if self.searchResult:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(2)
            name_item = QtWidgets.QTableWidgetItem(self.searchResult.getCourseInfo()[0])
            teacher_item = QtWidgets.QTableWidgetItem(self.searchResult.getCourseInfo()[2])
            self.tableWidget.setItem(0, 0, name_item)  # 클래스 이름 열에 추가
            self.tableWidget.setItem(0, 1, teacher_item)  # 교사 이름 열에 추가


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SearchCourse()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
