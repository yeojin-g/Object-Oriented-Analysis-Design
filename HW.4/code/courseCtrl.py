from course import Course
from tempDB import TempDB

class CourseCtrl:
    tempDB = TempDB()

    def createCourse(self, teacher = '', courseName = '', courseCode = ''):
        newCourse = Course(courseName, courseCode, teacher)
        self.tempDB.addCourse(courseName, newCourse)
        return newCourse
    
    def searchCourse(self, courseName):
        if self.tempDB.searchCourse(courseName):
            return self.tempDB.getCourse(courseName)
        else:
            print("존재하지 않는 Course")
            return False
            
    def joinCourseS(self, course, student):
        code = input()
        success = self.inputCode(code)
        if success:
            student.addCourse(course)
            return True
        else:
            return False
            
    def joinCourseP(self, course, parent):
        code = input()
        success = self.inputCode(code)
        if success:
            parent.addCourse(course)
            return True
        else:
            return False
    
    def delCourse(course):
        parentList = course.getParentList()
        teacherList = course.getTeacherList()
        studentList = course.StudentList()
        
        for i in [parentList, teacherList, studentList]:
            for j in i:
                j.delCourse(course)
        
        return course
    
    def inputCode(course, inputCode):
        courseCode = course.getCourseInfo()[1]        
        if courseCode == inputCode:
            return True
        else: return False