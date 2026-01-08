class student:
    student_USN="AB1234"
    student_marks=98.45
    def method1(self):
        self.student_group="Mathematics"
        return self.student_group
    def __shadow(self):
        self.passwd_aging=12456
        return self.passwd_aging
    __passwd_algm="SH51"

obj = student()
print(obj.student_USN)
print(obj.student_marks)
print(obj.method1())
print(obj.__shadow())