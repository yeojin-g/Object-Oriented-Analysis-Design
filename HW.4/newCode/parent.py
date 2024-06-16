from typing import Any
from user import User

class Parent(User):
    __childName = ""
    
    def __init__(self, name, id, pw, email, childName):
        super().__init__(name, id, pw, email)
        self.__childName = childName
        
    def getChildName(self):
        return self.__childName