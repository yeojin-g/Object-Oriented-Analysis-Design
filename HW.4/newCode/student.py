from user import User

class Student(User):
    __parentId = ""
    
    def __init__(self, name, id, pw, email):
        super().__init__(name, id, pw, email)
        
    def getParentId(self):
        return self.__parentId
    
    def setParentId(self, parentId):
        self.__parentId = parentId
