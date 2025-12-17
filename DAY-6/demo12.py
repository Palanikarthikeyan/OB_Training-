product={}
print(f'No.of items:{len(product)}')

count = 0
while( count < 5):
    pid = input('Enter a product ID:')
    pcost = input('Enter a product Cost:')
    product [pid] = pcost
    count += 1

print('Get List of Product details:-')
for var in product:
    print(f'{var} - {product[var]}')
    
print(f'\nNo.of items:{len(product)}')