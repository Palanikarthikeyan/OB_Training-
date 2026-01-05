class product1:
    pname = 'pA'
    pcost = 1000
    pcode = 101
    
class product2:
    pdescription = 'Sample data'
    
class customer(product1,product2):
    cus_id = 'C-101'
    
obj = customer()
print(obj.cus_id)
print(obj.pname,obj.pcost,obj.pcode)
print(obj.pdescription)