# 회원가입 팝업창

from PyQt5 import QtCore, QtWidgets

class UserRegister(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 314)

        # Ok Cancel 버튼박스
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        # "회원가입" 라벨
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 60, 16))
        self.label.setObjectName("label")

        # 아이디 입력창
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        # 비밀번호 입력창
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit) # 입력할 때만 문자를 표시하고, 수정 중에는 다른 문자를 표시합니다.

        # 사용자 이름 입력창
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 130, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        # 이메일 입력창
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 160, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")

        # "아이디" 라벨
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 60, 16))
        self.label_2.setObjectName("label_2")

        # "패스워드" 라벨
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 100, 60, 16))
        self.label_3.setObjectName("label_3")

        # "사용자 이름" 라벨
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 130, 60, 16))
        self.label_4.setObjectName("label_4")

        # "이메일" 라벨
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 160, 60, 16))
        self.label_5.setObjectName("label_5")

        # "교사" 라디오버튼
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(160, 190, 51, 20))
        self.radioButton.setObjectName("radioButton")

        # "사용자 유형" 라벨
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(90, 190, 60, 16))
        self.label_6.setObjectName("label_6")

        # "학생" 라디오버튼
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 190, 51, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        # "학부모" 라디오버튼
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(280, 190, 61, 20))
        self.radioButton_3.setObjectName("radioButton_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "회원가입")) 
        self.label.setText(_translate("Dialog", "회원가입"))
        self.label_2.setText(_translate("Dialog", "아이디"))
        self.label_3.setText(_translate("Dialog", "패스워드"))
        self.label_4.setText(_translate("Dialog", "사용자 이름"))
        self.label_5.setText(_translate("Dialog", "이메일"))
        self.radioButton.setText(_translate("Dialog", "교사"))
        self.label_6.setText(_translate("Dialog", "사용자 유형"))
        self.radioButton_2.setText(_translate("Dialog", "학생"))
        self.radioButton_3.setText(_translate("Dialog", "학부모"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UserRegister()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
