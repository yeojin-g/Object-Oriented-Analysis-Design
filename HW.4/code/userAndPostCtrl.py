from homework import Homework
from notice import Notice
from user import *
from course import Course
from personalHomework import PersonalHomework
from tempDB import TempDB

class UserAndPostCtrl:
    def __init__(self):
        pass 
       
    def createHomework(self, course, homeworkTitle, homeworkContent):
        newHW = Homework(homeworkTitle, homeworkContent)
        course.addHomework(newHW)
        return newHW
    
    def createNotice(self, course, noticeTitle, noticeContent):
        newNc = Notice(noticeTitle, noticeContent)
        course.addNoticeList(newNc)
        return newNc
    
    def gradeHomework(self, pHW, score, comment):
        pHW.setScore(score)
        pHW.setComment(comment)
        
    def delHomework(self, course, hw):
        delHomework = course.delHomework(hw)        
        return delHomework
    
    def delNotice(self, course, nc):
        delNotice = course.delNotice(nc)
        return delNotice
    
    def signIn(self, rolenum, name, Id, pw, email, pName = ''): #roleNum 0: 교사 / 1: 학생 / 2: 학부모
        tempDB = TempDB()
        newUser = ''
        try:
            if rolenum == 0:
                newUser = Teacher(name, Id, pw, email)
            elif rolenum == 1:
                newUser = Student(name, Id, pw, email)
            elif rolenum == 2:
                newUser = Parent(name, Id, pw, email, pName)
            else:
                print("유형을 선택해주세요")
                return False
            
            if tempDB.searchUser(Id): # DBList에 있는지
                print("이미 존재하는 사용자입니다.")
                return False

            tempDB.addUser(Id, newUser)
            return True
        except Exception as e:
            print(e)
            return False
    
    # def checkInfo(self, Id, pw): #Login
    #     try:
    #         if # id in db, id and pw correct
    #             return True
    #         else: return False
    #     except:
    #         print('error')
    #         return
            
            