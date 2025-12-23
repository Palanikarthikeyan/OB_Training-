class Enrollment:
    def __init__(self,emp_name,emp_dob):
        self.__emp_name = emp_name
        self.__emp_dob = emp_dob
        print(f'Emp {self.__emp_name} Enrollment is done')
    def __str__(self):
        return f'Emp name is:{self.__emp_name} dob is:{self.__emp_dob}'
    def __call__(self):
        return self.__emp_name,self.__emp_dob

eobj1 = Enrollment("Arun","1st Jan")

eobj2 = Enrollment("Leo","2nd Feb")

eobj3 = Enrollment("Anu","3rd March")

print('') # Empty line
print(str(eobj1))
print(str(eobj2))
print(str(eobj3))
print("") # empty line
print(eobj1())
print(eobj2())
print(eobj3())