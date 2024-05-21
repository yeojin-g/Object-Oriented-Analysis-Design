class TempDB:
    userList = {}
    
    def addUser(self, Id, User):
        self.userList[Id] = User
        print(self.userList)
        
    def searchUser(self, Id):
        if Id in self.userList.keys():
            return True
        else: 
            return False
        
    def getUser(self, Id):
        return self.userList[Id]

        