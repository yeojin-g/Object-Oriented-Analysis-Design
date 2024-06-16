class Homework:
    __title = ""
    __content = ""
    __submitStudentList = {} #name : pHomework
    
    def __init__(self, title, content):
        self.__title = title
        self.__content = content
        
    def getSubmitStudentList(self):
        return self.__submitStudentList
    
    def addStudent(self):
        pass