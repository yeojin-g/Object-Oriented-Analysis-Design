class User: # interface 역할
    userName = ''
    userID = ''
    userPassword = ''
    userEmail = ''
    courseList = []  # course 배열
    
    def getUserInfo(self):
        userInfoArr = [self.userName, self.userID, self.userPassword, self.userEmail]
        return userInfoArr
    
    def getCourseList(self):
        return self.courseList
    
    def setUserInfo(self, infoList):
        idx = 0
        for i in [self.userName, self.userID, self.userPassword, self.userEmail]:
            if infoList[idx] != '':
                i = infoList[idx]
                idx += 1
        # ['', '', 'pw123', ''] 로 배열이 들어올 경우 pw만 변경 나머지는 유지
        # 유지하고 싶은 정보의 경우 '' 값으로 주면 됨
        
    def addCourse(self, course):
        self.courseList.append(course)
    
    def delCourse(self, course):
        idx = self.courseList.index(course)
        delCourse = self.courseList.pop(idx)
        return delCourse
    

class Teacher(User):
    def __init__(self, name = '', Id = '', pw = '', email = ''):
        super().__init__(name, Id, pw, email)
        
class Parent(User):
    childName = ''
    def __init__(self, name = '', Id = '', pw = '', email = '', cName = ''):
        super.__init__(name, Id, pw, email)
        self.childName = cName
    
    def getCName(self):
        return self.childName
    
    def setCName(self, cname):
        self.childName = cname
        
class Teacher(User):
    parentName = ''
    def __init__(self, name = '', Id = '', pw = '', email = '', pName = ''):
        super.__init(name, Id, pw, email)
        self.parentName = pName
        
    def getPName(self):
        return self.parentName
    
    def setPName(self, pname):
        self.parentName = pname
    