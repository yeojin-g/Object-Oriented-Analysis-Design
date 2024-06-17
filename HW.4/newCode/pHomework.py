class PHomework:
    __score = 0
    __comment = ""
    __submitFile = None
    
    def __init__(self, submitFile):
        self.__submitFile = submitFile
        
    def setScoreAndComment(self, score, comment):
        self.__score = score
        self.__comment = comment