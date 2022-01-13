'''
Created on 13/1/2022
Course work: Python Basics
@author: saru , shruthi
Source: 
    
'''

def startpy():
    myfunc()


def myfunc():
         x = 3
         class MyClass(object):
             y = x
         return MyClass
print(myfunc().y)



if __name__ == '__main__':
      startpy()