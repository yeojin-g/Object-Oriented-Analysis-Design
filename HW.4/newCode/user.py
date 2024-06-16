class User:
    __name = ""
    __id = ""
    __pw = ""
    __email = ""
    __classList = {}
    
    def __init__(self, name, id, pw, email):
        self.__name = name
        self.__id = id
        self.__pw = pw
        self.__email = email
        
    def getInfoList(self):
        return [self.__name, self.__id, self.__pw, self.__email]
    
    def getClassList(self):
        return self.__classList
    
    def addClass(self, className, classObj):
        self.__classList[className] = classObj