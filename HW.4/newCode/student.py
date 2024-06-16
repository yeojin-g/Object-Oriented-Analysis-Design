from user import User

class Student(User):
    __parentName = ""
    
    def __init__(self, name, id, pw, email):
        super().__init__(name, id, pw, email)
        
    def setParentName(self):
        return self.__parentName
