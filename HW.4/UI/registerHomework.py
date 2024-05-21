# 과제 등록용 팝업창

from PyQt5 import QtCore, QtGui, QtWidgets


class RegisterHomework(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        # Ok Cancel 버튼박스
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        # "클래스 이름" 라벨
        self.label_courseName = QtWidgets.QLabel(Dialog)
        self.label_courseName.setGeometry(QtCore.QRect(130, 30, 60, 16))
        self.label_courseName.setObjectName("label_courseName")

        # "교사 이름" 라벨
        self.label_teacherName = QtWidgets.QLabel(Dialog)
        self.label_teacherName.setGeometry(QtCore.QRect(230, 30, 60, 16))
        self.label_teacherName.setObjectName("label_teacherName")

        # "과제 등록" 라벨
        self.label_registerHomework = QtWidgets.QLabel(Dialog)
        self.label_registerHomework.setGeometry(QtCore.QRect(170, 60, 60, 16))
        self.label_registerHomework.setObjectName("label_registerHomework")

        # "제목" 라벨
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(40, 90, 60, 16))
        self.label_title.setObjectName("label_title")

        # 제목 입력창
        self.lineEdit_title = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_title.setGeometry(QtCore.QRect(100, 90, 221, 21))
        self.lineEdit_title.setObjectName("lineEdit_title")

        # "내용" 라벨
        self.label_content = QtWidgets.QLabel(Dialog)
        self.label_content.setGeometry(QtCore.QRect(40, 120, 60, 16))
        self.label_content.setObjectName("label_content")

        # 내용 입력창
        self.textEdit_content = QtWidgets.QTextEdit(Dialog)
        self.textEdit_content.setGeometry(QtCore.QRect(100, 120, 221, 111))
        self.textEdit_content.setObjectName("textEdit_content")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_courseName.setText(_translate("Dialog", "수학")) # 클래스 이름 임시로 지정
        self.label_teacherName.setText(_translate("Dialog", "홍길동")) # 교사 이름 임시로 지정
        self.label_registerHomework.setText(_translate("Dialog", "과제 등록"))
        self.label_title.setText(_translate("Dialog", "제목"))
        self.label_content.setText(_translate("Dialog", "내용"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = RegisterHomework()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
