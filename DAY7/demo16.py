network={}

i=0
while(i < 5):
    host = input('Enter a hostname:')
    ip = input(f'Enter {host} IP Address:')
    network[host] = ip # adding new data to an existing dict
    i=i+1

print('Display - hostname and IPAddress')
for var in network:
    print(f'{var} - {network.get(var)}')
    
host = input('Enter a hostname:')
if(host in network):
    network[host] = '127.0.0.1'
    print('Updated - network details:')
    for var in network:
        print(f'{var} - {network.get(var)}')
else:
    print(f'Sorry host - {host} is not exists')