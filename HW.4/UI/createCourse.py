# 클래스 생성용 팝업창

from PyQt5 import QtCore, QtGui, QtWidgets

class CreateCourse(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        # Ok Cancel 버튼박스
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        # "클래스 생성" 라벨
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 40, 60, 16))
        self.label.setObjectName("label")

        # 클래스 이름 입력용
        self.lineEdit_className = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_className.setGeometry(QtCore.QRect(190, 100, 113, 21))
        self.lineEdit_className.setObjectName("lineEdit_className")

        # 확인 코드 입력용
        self.lineEdit_classCode = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_classCode.setGeometry(QtCore.QRect(190, 140, 113, 21))
        self.lineEdit_classCode.setObjectName("lineEdit_classCode")

        # "클래스 이름" 라벨
        self.label_className = QtWidgets.QLabel(Dialog)
        self.label_className.setGeometry(QtCore.QRect(110, 100, 60, 16))
        self.label_className.setObjectName("label_className")

        # "확인 코드" 라벨
        self.label_classCode = QtWidgets.QLabel(Dialog)
        self.label_classCode.setGeometry(QtCore.QRect(110, 140, 60, 16))
        self.label_classCode.setObjectName("label_classCode")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "클래스 생성"))
        self.label.setText(_translate("Dialog", "클래스 생성"))
        self.label_className.setText(_translate("Dialog", "클래스 이름"))
        self.label_classCode.setText(_translate("Dialog", "확인 코드"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = CreateCourse()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
