class Enrollment:
    emp_name = ''
    emp_dob = ''

eobj1 = Enrollment()
eobj1.emp_name = "Arun"
eobj1.emp_dob = "1st Jan"

eobj2 = Enrollment()
eobj2.emp_name = "Leo"
eobj2.emp_dob = "2nd Feb"

eobj3 = Enrollment()
eobj3.emp_name = "Anu"
eobj3.emp_dob = "3rd March"

print(f'Emp name:{eobj1.emp_name} dob is:{eobj1.emp_dob}')
print(f'Emp name:{eobj2.emp_name} dob is:{eobj2.emp_dob}')
print(f'Emp name:{eobj3.emp_name} dob is:{eobj3.emp_dob}')