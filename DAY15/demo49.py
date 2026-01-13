import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def method_operation(v):
	if v < 0:
		raise ValueError('Value - Not matched')
	else:
		logging.info('Operations is done') # normal execution


try:
	var = input('Enter some value:')
	method_operation(int(var))
except ValueError as eobj:
	logging.exception("Exception occurred:%s",str(eobj))