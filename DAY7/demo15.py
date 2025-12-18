'''
Given List:
Emp=['101,raj,sales,pune,1000',
     '102,leo,prod,bglore,2000',
     '103,anu,sales,hyd,3000',
     '104,zion,sales,bglore,3450']
'''
Emp=['101,raj,sales,pune,1000',
     '102,leo,prod,bglore,2000',
     '103,anu,sales,hyd,3000',
     '104,zion,sales,bglore,3450']

def display(dept='sales'): # default argument
    print(f"List of {dept} emp's records:-")
    print("------------------------------")
    total=0
    for var in Emp:
        if(dept in var):
            eid,ename,edept,ecity,ecost = var.split(",")
            print(f'Emp name is: {ename.title()}\t Working City: {ecity.upper()}')
            total = total + int(ecost)
        else:
            s = f'Sorry input dept {dept} is not exists from Emp Records'
    else:
        print(f"\t Sum of {dept} Emp's Cost:{total}")
        if(s):
            return s

#print(display())

#print(display('prod'))
print(display('devops'))