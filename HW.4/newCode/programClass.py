class Class:
    __className = ""
    __code = ""
    __teacherId = ""
    __parentList = {} # id: obj 
    __studentList = {} # id: obj 
    __homeworkList = {} # title: obj 
    __noticeList = {} # title: obj 
    
    def __init__(self, className, code, teacherId):
        self.__className = className
        self.__code = code
        self.__teacherId = teacherId
        
    def getClassInfo(self):
        return [self.__className, self.__code, self.__teacherId]
    
    def getParentList(self):
        return self.__parentList
    
    def getStudentList(self):
        return self.__studentList
    
    def addParent(self, parentID, parentObj):
        self.__parentList[parentID] = parentObj
        
    def addStudent(self, studentID, studentObj):
        self.__studentList[studentID] = studentObj
        
    def getHomeworkList(self):
        return self.__homeworkList
    
    def addHomework(self, title, homeworkObj):
        self.__homeworkList[title] = homeworkObj
    
    def getNoticeList(self):
        return self.__noticeList
    
    def addNotice(self, title, noticeObj):
        self.__noticeList[title] = noticeObj
    
    