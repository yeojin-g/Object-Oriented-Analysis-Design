from student import Student
from teacher import Teacher
from parent import Parent
from dbManager import DBManager

class UserCtrl:
    dbCtrl = DBManager()
    
    def signIn(self, roleNum, name, id, pw, email, childId = ""):
        newUser = None
        
        if not self.dbCtrl.searchUser(id):
            if roleNum == 0: #teacher
                newUser = Teacher(name, id, pw, email)
            elif roleNum == 1: #student
                newUser = Student(name, id, pw, email)
            elif roleNum == 2: #parent
                curChild = self.dbCtrl.searchUser(childId)
                if curChild:
                    newUser == Parent(name, id, pw, email, childId)
                    curChild.setParentId(id)
                else:
                    print("해당 ID의 자녀가 존재하지 않습니다.")
                    return False
            else:
                print("잘못된 role입니다.")
                return False
        else:
            print("이미 존재하는 사용자입니다")
            return False
        
        self.dbCtrl.addUser(roleNum, id, newUser)
        return True
        
    def Login(self, id, pw):
        loginUser = self.dbCtrl.searchUser(id)
        
        if loginUser:
            userPw = loginUser.getInfoList()[2]
            if userPw == pw:
                return loginUser
            else:
                print("비밀번호가 일치하지 않습니다.")
                return False
        else:
            print("존재하지 않는 사용자입니다.")
            return False
            
    def joinClass(self, userObj, className, classObj):
        userObj.addClass(className, classObj)
            