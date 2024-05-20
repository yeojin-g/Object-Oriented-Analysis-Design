class Homework:
    __homeworkTitle = ""
    __homeworkContent = ""
    __submitStudentList = []

    def __init__(self, title = '', content = ''):
        self.__homeworkTitle = title
        self.__homeworkContent = content

    def getTitle(self):
        return self.__homeworkTitle

    def getContent(self):
        return self.__homeworkContent

    def getPHomeworkList(self):
        return self.__submitStudentList

    def setTitle(self, title):
        self.__homeworkTitle = title

    def setContent(self, content):
        self.__homeworkContent = content

    def addPHomework(self, pHW):
        self.__submitStudentList.append(pHW)
        
    def delPHomework(self, pHW):
        idx= self.__submitStudentList.index(pHW)
        delPHomework = self.__submitStudentList.pop(idx)
        return delPHomework