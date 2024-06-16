# import sqlite3

class DBManager:
    __classList = {} # className: classObj
    __userList = {} # userId: [roleNum, userObj]
    
    # def dbInit(self):
    #     conn = sqlite3.connect("program.db")
    #     cur = conn.cursor()
    #     conn.execute('CREATE TABLE User(name TEXT, id TEXT, pw TEXT, email TEXT, roleNum INTEGER);') 
    #     conn.execute('CREATE TABLE Class(name Text, code Text, teacherID Text);')
    #     conn.execute('CREATE TABLE User_Class(userID text, );')
    #     conn.execute('CREATE TABLE Homework();')
    #     conn.execute('CREATE TABLE Notice();')
    #     conn.execute('CREATE TABLE Class_Homework();')
    #     conn.execute('CREATE TABLE Class_Notice();')
    #     conn.execute('CREATE TABLE PHomework();')
    #     conn.execute('CREATE TABLE Homework_PHomework();')
    
    def searchUser(self, userId):
        if userId in self.__userList.keys:
            return self.__userList[userId]
        else:
            return False
    
    def addUser(self, roleNum, userId, newUser):
        self.__userList[userId] = [roleNum, newUser]
        
    def searchClass(self, className):
        if className in self.__classList.keys:
            return self.__classList[className]
        else:
            return False

    def addClass(self, className, newClass):
        self.__classList[className, newClass]