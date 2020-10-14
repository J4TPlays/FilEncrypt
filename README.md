# FilEncrypt
## - by J4T
FilEncrypt is an open-source encryption algorithm written in Python 3. It is used for encrypting and decrypting data by using either random key generation or password-based key generation. 


## Usage
This distribution of FilEncrypt was designed to be imported as a module to make it easier to use in python programs. 

### Making a key
#### make_key( key_length = 1 , password = False )

The key length must be a positive integer greater than 0 so that the key can be generated. The password, however, is optional but must be in a **str** format. 

#### serialise( key )

Serialising the key will convert the key into a format that can either be sent or written to a file. 

#### read_key( key )

Reading the key returns the key in a format readable by FilEncrypt. 

#### encrypt( data , key ) 

Encrypts the data using the specified key. The password can not be used as the key, you must run the `make_key` function first. 

#### decrypt( data , key )

Decrypts the encrypted data using the specified key. The password can not be used as the key, you must `make_key` function first. 
