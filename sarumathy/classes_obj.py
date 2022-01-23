'''
Created on 13/1/2022
Course work: Python Basics
@author: saru , shruthi
Source: 
    
'''

def startpy():
    myfunc()
    stud()

def myfunc():
         x = 3
         class MyClass(object):
             y = x
         return MyClass
print(myfunc().y)

def stud():
    class Student:
        def __init__(self, name, rollno):
            self.name = name
            self.rollno = rollno

    p1 = Student("Saru", 18)

    print(p1.name)
    print(p1.rollno)


if __name__ == '__main__':
      startpy()