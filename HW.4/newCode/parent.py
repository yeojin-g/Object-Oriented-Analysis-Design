from typing import Any
from user import User

class Parent(User):
    __childId = ""
    
    def __init__(self, name, id, pw, email, childId):
        super().__init__(name, id, pw, email)
        self.__childId = childId
        
    def getChildId(self):
        return self.__childId