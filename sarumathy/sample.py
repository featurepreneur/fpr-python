'''
Created on 13/1/2022
Course work: Python Basics
@author: saru , shruthi
Source: 
    
'''

# Import necessary modules
import base64


def startpy():
     print("we are saru and shruthi")
     pass_state(7,6)
     tri_recursion(6)
     sort_eg([ "Shruthi", "Swedha", "Sarumathy", "Trishala" ])



def pass_state(a,b):
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
#print("\n\nRecursion Example Results")

def sort_eg(l_name):
  print (l_name)       # prints all elements
  l_name.sort()       # sorts the list in alphabetical order
  print(l_name)       # prints all elements





if __name__ == '__main__':
     startpy()
    