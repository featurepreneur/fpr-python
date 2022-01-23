'''
Created on 
Course work: 
@author: raja
Source:
    
'''

#plotform module 

import platform

def get_os_type():
    
    if (platform.system() == "Linux"):
        return(0)

    if (platform.system() == "Windows"):
        return(1)

    return(2)

def startpy():
    
    print(get_os_type())


if __name__ == '__main__':
    
    startpy()

