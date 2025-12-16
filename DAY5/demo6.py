'''
Task:
------
Write a python program:
|-> read a port number from <STDIN>
    test - input port range 5001-5999
	   ----------------------------
			|->initialize app name is demoApp

         - if port range is not matched with above range
			|->initialize app name is testApp
 
    display - app name running port number 
'''
port = input('Enter a port number:')
if(int(port) >5000 and int(port) <6000):
    app = "demoApp"
else:
    app = "testApp"

print(f'App name is:{app} running port number:{port}')
