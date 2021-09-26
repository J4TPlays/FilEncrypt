# FilEncrypt
## - by James "J4T" Forty
FilEncrypt is an open-source encryption algorithm written in Python 3. It is used for encrypting and decrypting data by using either random key generation or password-based key generation. This script is recommended either for FTP / Chat servers or encrypting files. 


## Usage (FilEncrypt.py)
This distribution of FilEncrypt was designed to be imported as a module to make it easier to use in python programs. 

### Making a key
#### make_key( key_length = 1 , password = False )

The key length must be a positive integer greater than 0 so that the key can be generated. The password, however, is optional but must be in a **str** format. You can run `make_key()` with no arguments and it will give a completely random key. The key length and password can both be changed to whatever the user chooses. 

### Making a layered key
#### layered_key( password , layers = 1, keylength = 1)

Creates a layered key by encrypting a key multiple times. The more layers, the more times the key gets encrypted. The key length is recommended to be larger than 1 for this to be effective, however.

### Serialising keys
#### serialise( key )

Serialising the key will convert the key into a format that can either be sent or written to a file. The size of this will always be a factor of 256 + 9, e.g. 256 + 9 = 265 bytes, 512 + 9 = 521 bytes, etc.

### Reading a serialised key
#### read_key( key )

Reading the key returns the key in a format readable by FilEncrypt. 

### Encrypting data
#### encrypt( data , key ) 

Encrypts the data using the specified key. The password can not be used as the key, you must run the `make_key` function first. 

### Decrypting data
#### decrypt( data , key )

Decrypts the encrypted data using the specified key. The password can not be used as the key, you must `make_key` function first. 




##
