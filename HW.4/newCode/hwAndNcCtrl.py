from homework import Homework
from dbManager import DBManager
from classCtrl import ClassCtrl

class HwAndNcCtrl:
    dbCtrl = DBManager()
    classCtrl = ClassCtrl()
    
    def regHw(self, title, content, classObj):
        if self.classCtrl.searchHw(title):
            print("동일한 내용의 과제가 이미 존재합니다.")
            return False
        else:
            newHw = Homework(title, content)
            self.classCtrl.addHomework(title, content, classObj)
            return True
            