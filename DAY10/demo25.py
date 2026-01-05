class product:
    pid = 101
    pname = 'pA'
    pcost = 1000
 

class customer(product):
    cid = "C-123"
    pcost = 'P-456-561'
    pa = product.pcost # To access parent class attribute
 

obj = customer()

print(obj.pid)
print(obj.pname)
print(obj.cid)
print(obj.pcost)
print(obj.pa)