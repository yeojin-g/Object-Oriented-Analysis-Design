class Homework:
    __title = ""
    __content = ""
    __submitStudentList = {} #id : pHomework
    
    def __init__(self, title, content):
        self.__title = title
        self.__content = content

    def getHomeworktitle(self):
        return self.__title
        
    def getSubmitStudentList(self):
        return self.__submitStudentList
    
    def addStudent(self, userName, pHwObj):
        self.__submitStudentList[userName] = pHwObj