# 프로그램 실행시 첫 메인화면

from PyQt5 import QtCore, QtGui, QtWidgets
from userLogin import UserLogin
from userRegister import UserRegister

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(503, 403)
        
        # icon 넣기
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # 로그인 툴버튼
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(130, 300, 121, 22))
        self.toolButton.setObjectName("toolButton")
        
        # 회원가입 툴버튼
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(260, 300, 121, 22))
        self.toolButton_2.setObjectName("toolButton_2")

        # "투게더 러닝" 라벨
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 260, 65, 31))
        self.label.setObjectName("label")

        # 이미지 삽입용 라벨
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(130, 50, 251, 181))
        self.label_image.setText("")
        self.pixmap = QtGui.QPixmap('icon.png') # 이미지 삽입을 위해 pixmap 사용
        self.label_image.setPixmap(self.pixmap) # 이미지 삽입을 위해 pixmap 사용
        self.label_image.setObjectName("label_image")
        
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.connectButton()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "투게더 러닝"))
        self.toolButton.setText(_translate("MainWindow", "로그인"))
        self.toolButton_2.setText(_translate("MainWindow", "회원가입"))
        self.label.setText(_translate("MainWindow", "투게더 러닝"))
        
    def connectButton(self): # 버튼과 전환함수 연결
        self.toolButton.clicked.connect(self.loginPage)
        self.toolButton_2.clicked.connect(self.signInPage)
        
    def loginPage(self): # 로그인 페이지로 전환하는 함수
        self.close()
        dialog = QtWidgets.QDialog()
        login = UserLogin()
        login.setupUi(dialog, self)
        dialog.exec_()
        
    def signInPage(self): # 회원가입 페이지로 전환하는 함수
        self.hide()
        dialog = QtWidgets.QDialog()
        signIn = UserRegister()
        signIn.setupUi(dialog)
        dialog.exec_()
        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
