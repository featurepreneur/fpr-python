'''
Created on 13/1/2022
Course work: Python Basics
@author: saru , shruthi
Source: 
    
'''

def startpy():
    display()


cse_c = { 
        "name " : "Sarumathy",
        "rollno": 18,
        "marks ": 50,
        "age": 15    
        }


def display():
    global cse_c
    cse_c["marks "]=49
    print(cse_c)






if __name__ == '__main__':
    startpy()