wobj = open('r1.log','w')

for var in range(5):
    ip_var = input('Enter some text:')
    wobj.write(ip_var+"\n")
    
wobj.close()
