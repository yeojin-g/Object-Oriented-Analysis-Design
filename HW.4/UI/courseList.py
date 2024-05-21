# 로그인하면 나오는 메인화면
# 클래스 검색, 클래스 생성을 할 수 있음 
# 로그인한 사용자의 클래스 목록이 [클래스이름, 교사이름] 형식으로 tableWidget으로 나오고 선택해서 입장할 수 있게 할 예정

from PyQt5 import QtCore, QtGui, QtWidgets

class CourseList(object):
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

        # "클래스 검색" 툴버튼
        self.toolButton_searchCourse = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_searchCourse.setGeometry(QtCore.QRect(100, 30, 111, 22))
        self.toolButton_searchCourse.setObjectName("toolButton_searchCourse")

        # "클래스 생성" 툴버튼
        self.toolButton_createCourse = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_createCourse.setGeometry(QtCore.QRect(270, 30, 121, 22))
        self.toolButton_createCourse.setObjectName("toolButton_createCourse")

        # 클래스 목록용 tableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 110, 291, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        # "클래스 입장" 툴버튼
        self.pushButton_enterClass = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enterClass.setGeometry(QtCore.QRect(190, 310, 113, 32))
        self.pushButton_enterClass.setObjectName("pushButton_enterClass")

        # "클래스 목록" 라벨
        self.label_classList = QtWidgets.QLabel(self.centralwidget)
        self.label_classList.setGeometry(QtCore.QRect(210, 80, 65, 16))
        self.label_classList.setObjectName("label_classList")
        
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "투게더 러닝"))
        self.toolButton_searchCourse.setText(_translate("MainWindow", "클래스 검색"))
        self.toolButton_createCourse.setText(_translate("MainWindow", "클래스 생성"))
        self.pushButton_enterClass.setText(_translate("MainWindow", "클래스 입장"))
        self.label_classList.setText(_translate("MainWindow", "클래스 목록"))