import time
fobj = open('my_pin_history.log','a')
pin = 1234
count = 0
while(count <3):
    count = count + 1
    p = input('Enter a pin Number:')
    if(int(p) == pin):
        fobj.write(f'Success pin is matched - {count} pin input date/time:{time.ctime()}\n')
        print(f'Success pin is matched - {count}')
        break
    else:
        fobj.write(f'Failed Sorry input pin:{p} is not matched. Pin input date/time:{time.ctime()}\n')

if(int(p) != pin):
    print('Sorry your pin is blocked')
    fobj.write(f'Sorry your pin is blocked - entry time is:{time.ctime()}\n')
    
fobj.close()