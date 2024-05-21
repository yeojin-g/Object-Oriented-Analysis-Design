from homework import Homework
from notice import Notice
from user import *
from course import Course
from personalHomework import PersonalHomework

class UserAndPostCtrl:    
    def createHomework(course, homeworkTitle, homeworkContent):
        newHW = Homework(homeworkTitle, homeworkContent)
        course.addHomework(newHW)
        return newHW
    
    def createNotice(course, noticeTitle, noticeContent):
        newNc = Notice(noticeTitle, noticeContent)
        course.addNoticeList(newNc)
        return newNc
    
    def gradeHomework(pHW, score, comment):
        pHW.setScore(score)
        pHW.setComment(comment)
        
    def delHomework(course, hw):
        delHomework = course.delHomework(hw)        
        return delHomework
    
    def delNotice(course, nc):
        delNotice = course.delNotice(nc)
        return delNotice
    
    def signIn(rolenum, name, Id, pw, email): #roleNum 0: 교사 / 1: 학생 / 2: 학부모
        if rolenum == 0:
            Teacher(name, Id, pw, email)
        elif rolenum == 1:
            Student(name, Id, pw, email)
        else:
            Parent(name, Id, pw, email. pName)
    
    def checkInfo(Id, pw): #Login
        try:
            if # id in db, id and pw correct
                return True
            else: return False
        except:
            print('error')
            return
            
            