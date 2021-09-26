"""

FilEncrypt
- by J4T

Binary encryption/decryption algorithm written in Python 3.

Version 1.0

~ Copyright © J4T 2020 ~
https://github.com/J4TPlays/FilEncrypt/

"""



import random as rd
import time



def make_key(keylength=1,password=False):
    if isinstance(keylength,int) and keylength>0:
        c=False
        if isinstance(password,str):
            rd.seed(password);c=True
        elif password==False:
            rd.seed(time.time());c=True
        if c:
            key=[]
            for i in range(256):
                t=[rd.randint(0,255) for i in range(keylength)]
                while t in key:t=[rd.randint(0,255) for i in range(keylength)]
                key.append(t)
            return key
        else:raise TypeError("Password must be str, not "+str(password.__class__.__name__))
    else:raise ValueError("Key length must be an integer greater than 0")



def serialise(key):             # serialises a key to be written or sent 
    try:return b"".join([bytes(i) for i in key])+b"/febinary"
    except:raise TypeError("The given key was not a valid FilEncrypt key")



def read_key(key):              # converts a serialised key to a readable format
    try:
        if (len(key)-9)%256==0:return [[x for x in key[i:i+(len(key)-9)//256]] for i in range(0,(len(key)-9),(len(key)-9)//256)]
        else:raise TypeError("The key given as not a valid FilEncrypt key")
    except:raise TypeError("The key given was not a valid FilEncrypt key")



def encrypt(data,key):
    if isinstance(data,bytes):
        try:return b"".join([bytes(x) for x in [key[i] for i in data]])
        except:raise TypeError("The key given was not a valid FilEncrypt key")
    else:raise TypeError("Data variable must be bytes, not "+data.__class__.__name__)



def decrypt(data,key):
    if isinstance(data,bytes):
        try:return bytes([key.index([i for i in bytes(data[i:i+len(key[0])])]) for i in range(0,len(data),len(key[0]))])
        except:raise TypeError("The key given was not a valid FilEncrypt key")
    else:raise TypeError("Data variable must be bytes, not "+data.__class__.__name__)
