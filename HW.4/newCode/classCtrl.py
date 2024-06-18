from programClass import Class
from dbManager import DBManager
from userCtrl import UserCtrl

class ClassCtrl:
    dbCtrl = DBManager()
    userCtrl = UserCtrl()
    testClass = Class("a", "b", "c")
    dbCtrl.addClass("a", testClass)
    
    
    def makeClass(self, className, code, teacherId):
        if not self.dbCtrl.searchClass(className): # 해당 이름의 class가 존재하지 않을 때
            newClass = Class(className, code, teacherId)
            
            self.dbCtrl.addClass(className, newClass) # DB classList에 추가
            teacherObj = self.dbCtrl.searchUser(teacherId)
            self.userCtrl.joinClass(teacherObj, className, newClass) # teacherClassList에 추가
            print("클래스 생성 성공")
            return True
        else:
            print("해당 이름의 클래스가 이미 존재합니다.")
            return False
    
    def searchClass(self, className):
        resultClass = self.dbCtrl.searchClass(className)
        
        if resultClass: # class 존재할 경우
            return resultClass
        else:
            print("class가 존재하지 않습니다.")
            return False
        
    def joinClass(self, roleNum, userId, userObj, classObj, code):
        className = classObj.getClassInfo()[0]
        classCode = classObj.getClassInfo()[1]
        print(classObj)
        print(className)
        print(classCode)
        
        if classCode == code:
            print("코드 일치, 가입 성공")
            
            self.userCtrl.joinClass(userObj, className, classObj) # user 객체에 클래스 추가
            if roleNum == 1: # 학생
                classObj.addStudent(userId, userObj)
            elif roleNum == 2: # 학부모
                classObj.addParent(userId, userObj)
            else:
                print("잘못된 roleNum입니다.")
                return False
            return True
        else:
            print("코드 불일치, 가입 실패")
            return False
            
    def searchHw(self, title, classObj):
        homeworkList = classObj.getHomeworkList()
        
        if title in homeworkList.keys():
            return homeworkList[title]
        else:
            print("해당 제목의 과제가 존재하지 않습니다.")
            return False
        
    def addHomework(self, title, homeworkObj, classObj):
        classObj.addHomework(title, homeworkObj)