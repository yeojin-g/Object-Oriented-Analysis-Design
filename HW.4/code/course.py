class Course:
    __courseName = ""
    __courseCode = ""
    __courseTeacher = ""
    __courseParentList = []
    __courseStudentList = []
    __homeworkList = []
    __noticeList = []


    def __init__(self, name = '', code = '', teacherName = ''):
        self.__courseName = name
        self.__courseCode = code
        self.__courseTeacher = teacherName

    def getCourseInfo(self):
        return [self.__courseName, self.__courseCode, self.__courseTeacher]

    def getParentList(self):
        return self.__courseParentList

    def getStudentList(self):
        return self.__courseStudentList

    def getHomeworkList(self):
        return self.__homeworkList

    def getNoticeList(self):
        return self.__noticeList

    def addParent(self, pr):
        self.__courseParentList.append(pr)

    def addStudent(self, std):
        self.__courseStudentList.append(std)

    def addHomework(self, hw):
        self.__homeworkList.append(hw)
        print("과제가 과제리스트에 등록되었습니다.")

    def addNoticeList(self, nc):
        self.__noticeList.append(nc)

    def setCourseInfo(self, nameAndCode):
        self.__courseName = nameAndCode[0]
        self.__courseCode = nameAndCode[1]

    def delHomework(self, hw):
        idx = self.__homeworkList.index(hw)
        delHomework = self.__homeworkList.pop(idx)
        return delHomework
    
    def delNotice(self, nc):
        idx = self.__noticeList.index(nc)
        delNotice = self.__noticeList.pop(idx)
        return delNotice
