class User: # interface 역할
    __userName = ''
    __userID = ''
    __userPassword = ''
    __userEmail = ''
    __courseList = []  # course 배열
    
    def getUserInfo(self):
        userInfoArr = [self.__userName, self.__userID, self.__userPassword, self.__userEmail]
        return userInfoArr
    
    def gedtCourseList(self):
        return self.__courseList
    
    def setUserInfo(self, infoList):
        idx = 0
        for i in [self.__userName, self.__userID, self.__userPassword, self.__userEmail]:
            if infoList[idx] != '':
                i = infoList[idx]
                idx += 1
        # ['', '', 'pw123', ''] 로 배열이 들어올 경우 pw만 변경 나머지는 유지
        # 유지하고 싶은 정보의 경우 '' 값으로 주면 됨
        
    def addCourse(self, course):
        self.__courseList.append(course)
    
    def delCourse(self, course):
        idx = self.__courseList.index(course)
        delCourse = self.__courseList.pop(idx)
        return delCourse
    

class Teacher(User):
    def __init__(self, name = '', Id = '', pw = '', email = ''):
        super().__init__(name, Id, pw, email)
        
class Parent(User):
    __childName = ''
    def __init__(self, name = '', Id = '', pw = '', email = '', cName = ''):
        super.__init__(name, Id, pw, email)
        self.__childName = cName
    
    def getCName(self):
        return self.__childName
    
    def setCName(self, cname):
        self.__childName = cname
        
class Student(User):
    __parentName = ''
    def __init__(self, name = '', Id = '', pw = '', email = '', pName = ''):
        super.__init(name, Id, pw, email)
        self.__parentName = pName
        
    def getPName(self):
        return self.__parentName
    
    def setPName(self, pname):
        self.__parentName = pname
        
        
