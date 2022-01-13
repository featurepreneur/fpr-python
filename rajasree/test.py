'''
Created on 
Course work: 
@author: rajasree
Source:
    
'''

# Import necessary modules
import base64


def startpy():
    text = encode("I am Rajasree")
    print(text)
    detext = decode(text)
    print(detext)


def encode(text):
    

    text_data = text
    ascii_data = text_data.encode('ascii')
    base64_byte_data = base64.b64encode(ascii_data)

    encoded_data = base64_byte_data.decode('ascii')
 
    return encoded_data


def decode(encoded_data):

    encoded_data = encoded_data


    base64_byte_data = encoded_data.encode('ascii')
    ascii_data = base64.b64decode(base64_byte_data)

    text_data = ascii_data.decode('ascii')
   
    return text_data


if __name__ == '__main__':
    startpy()