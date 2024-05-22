# 과제 제출용 팝업창

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QDialog
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'code'))
from personalHomework import PersonalHomework

class SubmitHomework(QDialog):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
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

        # "과제 파일 주소" 라벨
        self.label_submitHomework = QtWidgets.QLabel(Dialog)
        self.label_submitHomework.setGeometry(QtCore.QRect(20, 60, 370, 16))
        self.label_submitHomework.setObjectName("label_submitHomework")

        # "파일 선택" 푸시버튼
        self.pushButton_chooseFile = QtWidgets.QPushButton(Dialog)
        self.pushButton_chooseFile.setGeometry(QtCore.QRect(140, 90, 113, 32))
        self.pushButton_chooseFile.setObjectName("pushButton_chooseFile")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.submit) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_chooseFile.clicked.connect(self.chooseFile)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_homeworkTitle.setText(_translate("Dialog", "과제1")) # 과제 제목 임시로 지정
        self.label_studentName.setText(_translate("Dialog", "학생A"))    # 학생 이름 임시로 지정
        self.label_submitHomework.setText(_translate("Dialog", "")) # 과제 파일 주소
        self.pushButton_chooseFile.setText(_translate("Dialog", "파일 선택"))

    def chooseFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', './')
        if fname[0]:
            self.label_submitHomework.setText(fname[0])
            print('filepath : ', fname[0])
            print('filesort : ', fname[1])
            f = open(fname[0], 'r')

            with f:
                data = f.read()
        phw = PersonalHomework(data)
        print(phw.getFilename())

    def submit(self):
        #phw = PersonalHomework(self.chooseFile)
        #print(phw.getFilename())

        self.Dialog.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SubmitHomework()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
