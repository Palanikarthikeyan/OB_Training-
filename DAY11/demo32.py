import sys

fname = sys.argv[0]
if(len(sys.argv[1:]) == 0):
    print("Usage: Sorry your commandline is empty args")
    exit() # exit from python execution
    
if(len(sys.argv[1:]) != 2):
    print("Usage: Commandline args required any two numbers")
    print(f"python {sys.argv[0]} <Number1> <Number2>")
    exit() # exit from python execution
    
v1 = sys.argv[1]
v2 = sys.argv[2]

total = int(v1) + int(v2)
print(f'Sum of v1 + v2  value is:{total}')