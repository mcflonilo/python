class Student:
    passingMark = 50

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    def __str__(self):
        return f"{self.name} has {self.mark} marks"
    def passOrFail(self):
        if self.mark >= Student.passingMark:
            return "Pass"
        else:
            return "Fail"
        
student1 = Student("John", 52)
status1 = student1.passOrFail()
print(status1)
student2 = Student("Jenny", 69)
status2 = student2.passOrFail()
print(status2)

Student.passingMark = 60
status1 = student1.passOrFail()
status2 = student2.passOrFail()
print(status1)
print(status2)