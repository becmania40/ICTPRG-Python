import ipaddress #import ip function
while True:
    try:
        ipv4user = ipaddress.ip_address(input('Enter your IP address: ')) #user input
        break
    except ValueError: #error when not matching ip
        continue
print(ipv4user)