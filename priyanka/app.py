'''
Created on 
Course work: 
@author: raja
Source:
    
'''

# Import necessary modules
 

def startpy():


    print("Enter a word: ")

    word = str(input())

    count = 0
    
    for i in word:
        if (i.isupper()) == True:
            count = count + 1
    
    print(count)

if __name__ == '__main__':
    startpy()


