
'''
Created on 13/1/2022
Course work: Python Basics
@author: saru , shruthi
Source: 
    
'''





def startpy():

  diction(thisdict)
  access(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": [2020,1964,2018]
    }
   
def diction(thisdict):
  
  print(thisdict)

def access(thisdict):
  print(thisdict["year"][0])
  print(len(thisdict))
  x = thisdict.get("model")
  print(x)
  x1 = thisdict.keys()
  print(x1)


if __name__ == '__main__':
  startpy()




