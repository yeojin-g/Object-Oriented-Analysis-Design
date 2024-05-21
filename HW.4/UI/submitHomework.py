# 과제 제출용 팝업창

from PyQt5 import QtCore, QtGui, QtWidgets


class SubmitHomework(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 181)

        # Ok Cancel 버튼박스
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        # "과제 제목" 라벨
        self.label_homeworkTitle = QtWidgets.QLabel(Dialog)
        self.label_homeworkTitle.setGeometry(QtCore.QRect(130, 30, 60, 16))
        self.label_homeworkTitle.setObjectName("label_homeworkTitle")

        # "학생 이름" 라벨
        self.label_studentName = QtWidgets.QLabel(Dialog)
        self.label_studentName.setGeometry(QtCore.QRect(230, 30, 60, 16))
        self.label_studentName.setObjectName("label_studentName")

        # "과제 제출" 라벨
        self.label_submitHomework = QtWidgets.QLabel(Dialog)
        self.label_submitHomework.setGeometry(QtCore.QRect(170, 60, 60, 16))
        self.label_submitHomework.setObjectName("label_submitHomework")

        # "파일 선택" 푸시버튼
        self.pushButton_chooseFile = QtWidgets.QPushButton(Dialog)
        self.pushButton_chooseFile.setGeometry(QtCore.QRect(140, 90, 113, 32))
        self.pushButton_chooseFile.setObjectName("pushButton_chooseFile")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_homeworkTitle.setText(_translate("Dialog", "과제1")) # 과제 제목 임시로 지정
        self.label_studentName.setText(_translate("Dialog", "학생A"))    # 학생 이름 임시로 지정
        self.label_submitHomework.setText(_translate("Dialog", "과제 제출"))
        self.pushButton_chooseFile.setText(_translate("Dialog", "파일 선택"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SubmitHomework()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
