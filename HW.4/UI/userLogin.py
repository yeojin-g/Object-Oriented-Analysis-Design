from PyQt5 import QtCore, QtWidgets
from courseList import CourseList

class UserLogin(object):
    def setupUi(self, Dialog, mainWindow):
        self.curPage = Dialog
        self.mainWindow = mainWindow 
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 312)
        
        # Ok Cancel 버튼 박스
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        # "로그인" 라벨
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 30, 60, 16))
        self.label.setObjectName("label")

        # 아이디 입력창
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 110, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        # 비밀번호 입력창
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 150, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit) # 입력할 때만 문자를 표시하고, 수정 중에는 다른 문자를 표시합니다.

        # "아이디" 라벨
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 60, 16))
        self.label_2.setObjectName("label_2")

        # "패스워드" 라벨
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 150, 61, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.courseList) # courseList 페이지로 전환하는 함수 연결
        self.buttonBox.rejected.connect(self.cancelLogin) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "로그인"))
        self.label.setText(_translate("Dialog", "로그인"))
        self.label_2.setText(_translate("Dialog", "아이디"))
        self.label_3.setText(_translate("Dialog", "패스워드"))


    def courseList(self): # courseList 페이지로 전환하는 함수
        self.curPage.close()  
        nextPage = CourseList()  
        nextPage.setupUi(self.curPage)  
        self.curPage.show()    

    def cancelLogin(self): # 취소 버튼 클릭 시 메인 윈도우 보여주는 함수
        self.curPage.close()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = UserLogin()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
