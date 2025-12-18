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

print("List of sales emp's records:-")
print("------------------------------")
total=0
for var in Emp:
    if('sales' in var):
        eid,ename,edept,ecity,ecost = var.split(",")
        print(f'Emp name is: {ename.title()}\t Working City: {ecity.upper()}')
        total = total + int(ecost)
else:
    print(f"\t Sum of Sales Emp's Cost:{total}")
