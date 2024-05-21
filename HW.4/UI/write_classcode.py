# 클래스를 검색해서 가입할 때 확인코드를 입력하기 위한 팝업창

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 136)

        # Ok Cancel 버튼박스
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        # 클래스 코드 입력창
        self.lineEdit_classCode = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_classCode.setGeometry(QtCore.QRect(190, 40, 113, 21))
        self.lineEdit_classCode.setObjectName("lineEdit_classCode")

        # "클래스 코드" 라벨
        self.label_classCode = QtWidgets.QLabel(Dialog)
        self.label_classCode.setGeometry(QtCore.QRect(100, 40, 60, 16))
        self.label_classCode.setObjectName("label_classCode")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_classCode.setText(_translate("Dialog", "클래스 코드"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
