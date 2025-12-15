'''
Write a python program:
 
- read a product details (name,product ID,product Cost) from <STDIN>
- Calculate 18% of product cost and initialize to new variable called tax
- Calculate Sum of productCost including tax
- display product details - use print() 

Expected Result:-
--------------------
Product name is: pA
Product ID is: 123
Product Cost is: 1000
18% Tax is: 180
Total including Tax: 1180 Rs
--------------------------------
'''
pname = input('Enter a product name:')
pid = input(f'Enter {pname} ID:')
pcost = input(f'Enter {pname} Cost:')
tax = 0.18 * float(pcost)
total = tax + float(pcost)
print(f'''Product name:{pname}
------------------------------
Product ID:{pid}
------------------------------
Product Cost is:{pcost}
------------------------------
18 % Tax amount:{tax}
------------------------------
Total Cost including Tax:{total}
---------------------------------''')