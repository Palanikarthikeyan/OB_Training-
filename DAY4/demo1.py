'''
Write a python program:
 
- initialize a product name,product ID,product Cost
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
Docstring for demo1
'''
pname = 'pA'
pid = 123
pcost = 1000
tax = 0.18 * pcost
total = tax + pcost
print('Product name:'+pname)
print('Product ID:'+str(pid))
print('Product Cost is:'+str(pcost))
print('18 % Tax amount:'+str(tax))
print('Total Cost including Tax:'+str(total))