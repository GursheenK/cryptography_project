#VIGNERE CIPHER
#Ei=(Pi+ki)%26
#Di=(Ei-Ki+26)%26
import math

def encrypt_words(plain_text,key):
    cipher_text=''
    n=len(plain_text)
    ceil_val=math.ceil(n/len(key))
    key=ceil_val*key
    for i in range(n):
        if plain_text[i]==' ':
            cipher_text+=' '
        elif plain_text[i].islower():
            pi=ord(plain_text[i])-97
            ki=ord(key[i])-97
            ei=(pi+ki)%26
            cipher_text+=chr(ei+97)
        else:
            pi=ord(plain_text[i])-65
            ki=ord(key[i])-65
            ei=(pi+ki)%26
            cipher_text+=chr(ei+65)
    return cipher_text

def decrypt_words(cipher_text,key):
    plain_text=''
    n=len(cipher_text)
    ceil_val=math.ceil(n/len(key))
    key=ceil_val*key
    for i in range(n):
        if cipher_text[i]==' ':
            plain_text+=' '
        elif cipher_text[i].islower():
            ei=ord(cipher_text[i])-97
            ki=ord(key[i])-97
            di=(ei-ki+26)%26
            plain_text+=chr(di+97)
        else:
            ei=ord(cipher_text[i])-65
            ki=ord(key[i])-65
            di=(ei-ki+26)%26
            plain_text+=chr(di+65)
    return plain_text
