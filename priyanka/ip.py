'''
Created on 
Course work: 
@author: raja
Source:
    
'''

# importing ip_address from 
# ip address module

from ipaddress import ip_address

def get_ip_type(ip: str) -> str:
    
    if(ip is None):
        return "None is not accepted"

    try:
        if (ip_address(ip).is_private):
            return "Private"
    except ValueError as ip_err:
        return "Not a valid IP Format"

    return "Public"

def startpy():
    
    print(get_ip_type("10.255.255.255"))

if __name__ == '__main__' : 
   
   startpy()
  
    

