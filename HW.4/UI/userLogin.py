import os
import sys
from PyQt5 import QtCore, QtWidgets
from courseList import CourseList
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'code'))
from userAndPostCtrl import UserAndPostCtrl

class UserLogin(object):
    def setupUi(self, Dialog, main):
        self.curPage = Dialog
        self.main = main
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 312)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 30, 60, 16))
        self.label.setObjectName("label")
        self.label.setText("로그인")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 110, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 150, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("아이디")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 150, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("패스워드")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.courseList)
        self.buttonBox.rejected.connect(self.cancelLogin)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "로그인"))

    def courseList(self):
        userCtrl = UserAndPostCtrl()
        Id = self.lineEdit.text()
        pw = self.lineEdit_2.text()

        loginSuccess = userCtrl.checkInfo(Id, pw)

        if loginSuccess:
            self.curPage.close()

            nextPage = CourseList()
            nextPage.setupUi(self.main)
            QtWidgets.QMessageBox.information(self.curPage, 'Success', '로그인 성공.')
            self.main.show()
        else:
            QtWidgets.QMessageBox.warning(self.curPage, 'Error', '로그인 실패. 아이디와 비밀번호를 확인하세요.')


    def cancelLogin(self):
        self.curPage.reject()
        self.main.show()
