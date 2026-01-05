try:
    fobj = open('pop.log','r')
except Exception as eobj:
    print(eobj)
else:
    s = fobj.read()
    print(s)
    fobj.close()
    
print('Next Section of code')
for v in range(3):
    print('data')
    