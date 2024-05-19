class Course:
    __courseName = ""
    __courseCode = ""
    __courseTeacher = ""
    __courseParentList = []
    __courseStudentList = []
    __homeworkList = []
    __noticeList = []


    def __init__(self, name, code, teacherName):
        self.__courseName = name
        self.__courseCode = code
        self.__courseTeachdr = teacherName

    def getCourseInfo(self):
        return self.__courseName, self.__courseCode, self.__courseTeacher

    def getParentList(self):
        return self.__courseParentList

    def getStudentList(self):
        return self.__courseStudentList

    def getHomeworkList(self):
        return self.__homeworkList

    def getNoticeList(self):
        return self.__noticeList

    def addParent(pr):
        self.__courseParentList.append(pr)

    def addStudent(std):
        self.__courseStudentList.append(std)

    def addHomework(hw):
        self.__homeworkList.append(hw)

    def addNoticeList(nc):
        self.__noticeList.append(nc)

    def setCourseInfo(nameAndCode):
        self.__courseName = nameAndCode[0]
        self.__courseCode = nameAndCode[1]

    def delHomework(hw):
        self.__homeworkList.remove(hw)

    def delNotice(nc):
        self.__noticeList.remove(nc)