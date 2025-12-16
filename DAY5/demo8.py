'''
read a input string from keyboard (ex: 101,raj,sales,hyderabad,1000)
|
test - pattern sales is matched or not
			|	     |->pattern sales is not exists
			|
			Given string pattern sales is exists
'''
input_data = input('Enter some text:')
pattern = 'sales'

if(pattern in input_data):
    print(f'Yes Given pattern:{pattern} is exists')
else:
    print(f'Sorry pattern {pattern} is not found.')
