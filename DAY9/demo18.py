'''
Write a python program:
---------------------
create employee enrollment class
 - initialize following attributes
	emp_name
	emp_id
	emp_cost
	emp_DOB

 - using class - display emp details
 |
 - using class - update/modify emp_cost
 - using class - display blood_group ->AttributeError
 |
 - initialize blood_group and display it.

'''
class Enrollment:
    emp_id = 0
    emp_name = ''
    emp_cost = 0.0
    emp_DOB = ''

print(Enrollment.emp_id)
print(Enrollment.emp_name)
print(Enrollment.emp_cost)
print(Enrollment.emp_DOB)
Enrollment.emp_cost = 1000
print(Enrollment.emp_cost)
print(Enrollment.emp_cost)

#print(Enrollment.blood_group)
Enrollment.blood_group = 'A+'
print(Enrollment.blood_group)
Enrollment.city_name = ''

Enrollment.emp_id=505
Enrollment.emp_id


