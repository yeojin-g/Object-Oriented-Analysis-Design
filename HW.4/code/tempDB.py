from course import  Course

class TempDB:
    userList = {}
    # courseList = {}
    courseList = {'aa': Course('aa', 00), 'bb': Course('bb', 11)}

    def addUser(self, Id, User):
        self.userList[Id] = User
        print(self.userList)
        
    def searchUser(self, Id):
        if Id in self.userList.keys():
            return True
        else: 
            return False
        
    def getUser(self, Id):
        return self.userList[Id]

    def addCourse(self, name, Course):
        self.courseList[name] = Course
        print(self.courseList)

    def searchCourse(self, name):
        if name in self.courseList.keys():
            return True
        else:
            return False

    def getCourseList(self):
        return self.courseList

    def getCourse(self, name):
        return self.courseList[name]
