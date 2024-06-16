from user import User

class Teacher(User):
    def __init__(self, name, id, pw, email):
        super().__init__(name, id, pw, email)
        