'''
Task
-----
Write a python program:
 |-> create an empty list
 |-> initialize a pin number (ex: pin = 1234)
 |-> use while loop - limit is 3
	 ===========
	  |-> read a pin Number from <STDIN>
	  |-> test - input pin matched with an existing pin 
		   - display - pin success - <Count> (ex: pin is matched - 1/2/3)
         # add - user input details to list
 |-> if all 3 inputs are failed - pin is blocked.
 |-> read a option from <STDIN> (Wish to read input pin details? Yes | YES):
 |->display list of items(pin details)
'''
pin_history = []
pin = 1234
count = 0
while(count < 3):
    p = input('Enter a pin Number:')
    count = count+1
    if(int(p) == pin):
        pin_history.append(f'Success pin is matched - {count}')
        print(f'Success pin is matched - {count}')
        break
    else:
        pin_history.append(f'Failed - input pin:{p}')

if(int(p) != pin):
    pin_history.append('Sorry your pin is blocked')
    print('Sorry your pin is blocked')        

choice = input('Wish to read/see user pin details:-')
if(choice == "Yes" or choice == "Y" or choice == "yes"):
    for var in pin_history:
        print(var)
