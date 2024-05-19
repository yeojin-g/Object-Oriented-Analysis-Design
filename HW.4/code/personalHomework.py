class PersonalHomework:
    __submitFile = ""
    __score = 0
    __comment = ""

    def __init__(self, submitFile):
        self.__submitFile = submitFile

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

    score = property(getScore, setScore)
    comment = property(getComment, setComment)