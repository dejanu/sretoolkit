#!/usr/bin/env python

import string
alphabet = string.ascii_lowercase
Alphabet = string.ascii_uppercase

def caesarCipher(s, k):
    # s - string to be encrypted
    # k - int no of rotations
    new_data = ''
    for c in s:
        if c.isupper():
            index = Alphabet.find(c)
            if index == -1:
                # Character not found
                new_data += c
            else:
                # Shift it based on key
                new_index = (index + k) % 26
                new_data += Alphabet[new_index:new_index+1]
        else:
            # Shift character
            index = alphabet.find(c)
            if index == -1:
                # Character not found
                new_data += c
            else:
                # Shift it based on key
                new_index = (index + k) % 26
                new_data += alphabet[new_index:new_index+1]
    # Return the ciphered text
    return new_data   