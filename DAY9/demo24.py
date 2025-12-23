class Enrollment:
    @classmethod
    def f1(cls,emp_name,emp_dob):
        cls.emp_name = emp_name
        cls.emp_dob = emp_dob
    def initialization(self,emp_name,emp_dob):
        self.emp_name = emp_name
        self.emp_dob = emp_dob
        print(f'Emp {self.emp_name} Enrollment is done')
    def display(self):
        print(f'Emp name is:{self.emp_name} dob is:{self.emp_dob}')

Enrollment.f1('default_emp_Name','default_emp_dept')
eobj1 = Enrollment()
eobj1.initialization("Arun","1st Jan")
eobj1.display()

eobj2 = Enrollment()
eobj2.display() # AttributeError 
eobj3 = Enrollment()
eobj3.initialization("Leo","2nd Feb")
eobj3.display()
