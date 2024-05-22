class PersonalHomework:
    __submitFile = ""
    __score = 0
    __comment = ""

    def __init__(self, submitFile):
        self.__submitFile = submitFile
        print("제출 파일이 선택되었습니다.")

    def setScore(self, score):
        self.__score = score

    def setComment(self, cmt):
        self.__comment = cmt

    def getFilename(self):
        return self.__submitFile

    def getScore(self):
        return self.__score

    def getComment(self):
        return self.__comment