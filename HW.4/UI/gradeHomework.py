# 성적 채점용 팝업창

from PyQt5 import QtCore, QtGui, QtWidgets


class GradeHomework(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        # Ok Cancel 버트박스
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
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

        # "과제 채점" 라벨
        self.label_gradeHomework = QtWidgets.QLabel(Dialog)
        self.label_gradeHomework.setGeometry(QtCore.QRect(170, 60, 60, 16))
        self.label_gradeHomework.setObjectName("label_gradeHomework")

        # "점수" 라벨
        self.label_score = QtWidgets.QLabel(Dialog)
        self.label_score.setGeometry(QtCore.QRect(40, 90, 60, 16))
        self.label_score.setObjectName("label_score")

        # 점수 입력창
        self.lineEdit_score = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_score.setGeometry(QtCore.QRect(100, 90, 221, 21))
        self.lineEdit_score.setObjectName("lineEdit_score")

        # "코멘트" 라벨
        self.label_comment = QtWidgets.QLabel(Dialog)
        self.label_comment.setGeometry(QtCore.QRect(40, 120, 60, 16))
        self.label_comment.setObjectName("label_comment")

        # 코멘트 입력창
        self.textEdit_comment = QtWidgets.QTextEdit(Dialog)
        self.textEdit_comment.setGeometry(QtCore.QRect(100, 120, 221, 111))
        self.textEdit_comment.setObjectName("textEdit_comment")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_homeworkTitle.setText(_translate("Dialog", "과제1")) # 과제 제목 임시로 지정
        self.label_studentName.setText(_translate("Dialog", "학생A"))    # 학생 이름 임시로 지정
        self.label_gradeHomework.setText(_translate("Dialog", "과제 채점"))
        self.label_title.setText(_translate("Dialog", "점수"))
        self.label_content.setText(_translate("Dialog", "코멘트"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = GradeHomework()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
