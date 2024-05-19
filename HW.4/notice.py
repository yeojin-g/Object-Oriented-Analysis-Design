class Notice:
    __noticeTitle = ""
    __noticeDate = ""
    __noticeContent = ""
    __readCount = 0
    def __init__(self, title, content):
        self.__noticeTitle = title
        self.__noticeContent = content

    def getNoticeInfo(self):
        return self.__noticeTitle, self.__noticeDate, self.__noticeContent, self.__readCount

    def countHits(self):
        self.__readCount =+ 1

    def setTitle(self, title):
        self.__noticeTitle = title

    def setContent(self, content):
        self.__noticeContent = content