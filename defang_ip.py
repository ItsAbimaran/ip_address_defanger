#ip address defanger
import socket
def ip(ip_address): 
    b=""
    for i in ip_address:
        if i== '.':
           b+='[]'
        else:
            b+=i
    return b

print("If you know  the ip address-write 'yes'")
print("If you want to get ip address from the local-'no'")
a=input('yes/no')
if a=="no":
   hostname=socket.gethostname()
   ip_address=socket.gethostbyname(hostname)
   addr=ip(ip_address)
else:
    ip_address=input("enter ur ip address")
    addr=ip(ip_address)
print("enter an IP address:",ip_address)
print("Original IP address:",ip_address) 
print("Defanged IP address:",addr);


