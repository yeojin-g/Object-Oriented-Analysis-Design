from homework import Homework
from pHomework import PHomework
from dbManager import DBManager
from classCtrl import ClassCtrl

class HwCtrl:
    dbCtrl = DBManager()
    classCtrl = ClassCtrl()
    
    def regHw(self, title, content, classObj):
        if self.classCtrl.searchHw(title, classObj):
            print("동일한 내용의 과제가 이미 존재합니다.")
            return False
        else:
            newHw = Homework(title, content)
            self.classCtrl.addHomework(title, newHw, classObj)
            return True
            
    def gradeHw(self, score, comment, pHwObj):
        if score >= 0 & comment:
            pHwObj.setScoreAndComment(score, comment)
            return True
        else:
            print("Score 혹은 Comment 형식이 올바르지 않습니다.")
            return False
        
    def submitHw(self, userName, hwFile, hwObj):
        newPHw = PHomework(hwFile)
        try:
            hwObj.addStudent(userName, newPHw)
            return True
        except:
            print("error")
            return False
        
    def checkHw(self, childName, hwObj):
        stdList = hwObj.getSubmitStudentList()
        
        if childName in stdList:
            return stdList[childName]
        else:
            print("제출된 과제가 존재하지 않습니다.")
            return False
        