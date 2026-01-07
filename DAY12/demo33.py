pin = 1234
count = 0
while(count <3):
    count = count + 1
    p = input('Enter a pin Number:')
    if(int(p) == pin):
        print(f'Success pin is matched - {count}')
        break

if(int(p) != pin):
    print('Sorry your pin is blocked')