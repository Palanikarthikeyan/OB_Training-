class Enrollment:
    def __init__(self,emp_name,emp_dob):
        self.emp_name = emp_name
        self.emp_dob = emp_dob
        print(f'Emp {self.emp_name} Enrollment is done')
    def display(self):
        print(f'Emp name is:{self.emp_name} dob is:{self.emp_dob}')

eobj1 = Enrollment("Arun","1st Jan")
#eobj1.initialization("Arun","1st Jan")

eobj2 = Enrollment("Leo","2nd Feb")
#eobj2.initialization("Leo","2nd Feb")

eobj3 = Enrollment("Anu","3rd March")
#eobj3.initialization("Anu","3rd March")

print('') # Empty line

for var in [eobj1,eobj2,eobj3]:
    var.display()
    print('') # Empty line
