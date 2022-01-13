'''
Created on 
Course work: 
@author: rajasree
Source:
    
'''

# Import necessary modules
import base64
encoded_data = ""

def startpy():
    encode("I am Rajasree")
    decode(encoded_data)

def encode(text):
    

    text_data = text
    ascii_data = text_data.encode('ascii')
    base64_byte_data = base64.b64encode(ascii_data)

    encoded_data = base64_byte_data.decode('ascii')
    print(encoded_data)
    return encoded_data


def decode(encoded_data):

    encoded_data = encoded_data


    base64_byte_data = encoded_data.encode('ascii')
    ascii_data = base64.b64decode(base64_byte_data)

    text_data = ascii_data.decode('ascii')
    print(text_data)
    return text_data


if __name__ == '__main__':
    startpy()