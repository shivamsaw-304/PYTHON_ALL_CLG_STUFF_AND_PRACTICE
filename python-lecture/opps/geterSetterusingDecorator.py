class Student:

    def __init__(self):
        self.__marks = 0

    @property
    def geterMarks(self):
        return self.__marks



    @geterMarks
    def setterMarks(self,number):
        self.__marks = number


Student = Student()
Student.setterMarks(20)
