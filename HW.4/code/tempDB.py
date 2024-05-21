class TempDB:
    userList = {}
    
    def addUser(self, id, User):
        self.userList[id] = User
        
    def searchUser(self, id):
        if id in self.userList.keys:
            return self.userList[id]
        else: return False