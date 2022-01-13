'''
Created on 
Course work: 
@author: rajasree
Source:
    
'''

# Import necessary modules
import base64


def startpy(a,b):
     if(a>b):
         pass       # null statement
     else:
         print("b<a")


def tri_recursion(a):
  if(a > 0):
    result = a + tri_recursion(a- 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")


l_name = [ "Shruthi", "Swedha", "Sarumathy", "Trishala" ]
print (l_name)       # prints all elements
l_name.sort()       # sorts the list in alphabetical order
print(l_name)       # prints all elements





if __name__ == '__main__':
     startpy(7,6)
     tri_recursion(6)