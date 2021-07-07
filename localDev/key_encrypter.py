#!/usr/bin/python3


from cryptography.fernet import Fernet



## generate key for encryption as bytes one time :X
# with open("vault", "wb") as f:
#     f.write(Fernet.generate_key())


def encrypt_it(msg,fkey):
    """ encrypt msg using fernet obj """
    f = Fernet(fkey)
    msg_encoded = f.encrypt(msg)
    return msg_encoded
    
def decrypt_it(emsg,fkey):
    """ decrypt msg using fernet obj"""
    f = Fernet(fkey)
    msg_decoded = f.decrypt(emsg)
    return msg_decoded



    

if __name__ == "__main__":
    
 
    # encrypt passwords 
    encrypt_msg = encrypt_it(b"messagetoencrypt", <key_generated_onetime>)
    # usage decrypt_it(encrypt_msg,<key_generated_onetime>)
