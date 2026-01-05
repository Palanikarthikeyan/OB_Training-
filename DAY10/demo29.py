try:
   n = input('Enter n Value')
   if(int(n) >500 and int(n) <600):
       raise ValueError('Invalid Port Range')
except ValueError as eobj:
    print(eobj)