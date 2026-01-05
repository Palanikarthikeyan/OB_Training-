print("one")
print("two")
print("three")
try:
    print(four)
except Exception as eobj:
    print(eobj)
print("five")
print("six")
try:
    d={'K1':'V1'}
    print(d['K2'])
except Exception as eobj:
    print(eobj)
else:
    print('No Exception')