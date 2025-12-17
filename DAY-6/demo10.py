'''
Task
-----
Write a python program:
 |-> initialize a pin number (ex: pin = 1234)
 |-> use while loop - limit is 3
	 ===========
	  |-> read a pin Number from <STDIN>
	  |-> test - input pin matched with an existing pin 
		   - display - pin success - <Count> (ex: pin is matched - 1/2/3)

 |-> if all 3 inputs are failed - pin is blocked.
'''
pin = 1234
count = 0
while(count < 3):
    p = input('Enter a pin Number:')
    count = count+1
    if(int(p) == pin):
        print(f'Success pin is matched - {count}')
        break

if(int(p) != pin):
    print('Sorry your pin is blocked')        
