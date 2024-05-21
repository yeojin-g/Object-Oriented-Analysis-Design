# 프로그램 실행시 첫 메인화면

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 403)
        
        # icon 넣기
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.label.setGeometry(QtCore.QRect(220, 260, 61, 31))
        self.label.setObjectName("label")

        # 이미지 삽입용 라벨
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(130, 50, 251, 181))
        self.label_image.setText("")
        self.pixmap = QtGui.QPixmap('icon.png') # 이미지 삽입을 위해 pixmap 사용
        self.label_image.setPixmap(self.pixmap) # 이미지 삽입을 위해 pixmap 사용
        self.label_image.setObjectName("label_image")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "투게더 러닝"))
        self.toolButton.setText(_translate("MainWindow", "로그인"))
        self.toolButton_2.setText(_translate("MainWindow", "회원가입"))
        self.label.setText(_translate("MainWindow", "투게더 러닝"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
