from programClass import Class

class DBManager:
    __classList = {"123": Class("123", "123", "123")} # className: classObj
    __userList = {} # userId: [roleNum, userObj]
    
    
    def searchUser(self, userId):
        if str(userId) in self.__userList.keys():
            return self.__userList[userId][1]
        else:
            return False
    
    def addUser(self, roleNum, userId, newUser):
        self.__userList[userId] = [roleNum, newUser]
        print(self.__userList)
        
    def searchClass(self, className):
        if className in self.__classList.keys():
            return self.__classList[className]
        else:
            return False

    def addClass(self, className, newClass):
        self.__classList[className] = newClass