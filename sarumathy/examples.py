'''
Created on 16/1/2022
Course work: Python Basics
@author: saru 
Source: 
    
'''


def startpy():
    employ()


def employ():
    class Employee:
        empCount = 0

        def __init__(self, name, salary):
            self.name = name
            self.salary = salary
            Employee.empCount += 1
   
        def displayCount(self):
            print ("Total Employee :" + Employee.empCount)

        def displayEmployee(self):
            print ("Name : ", self.name,  ", Salary: ", self.salary)

    emp1 = Employee("Kohli", 18000)
    emp2 = Employee("Rohit", 4500)
    emp1.displayEmployee()
    emp2.displayEmployee()
    empp3= Employee("Rahul", 1200)
    empp3.displayEmployee()
    print ("Total Employee " , Employee.empCount)







if __name__ == '__main__':
    startpy()
