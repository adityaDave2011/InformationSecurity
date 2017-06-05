#!/usr/bin/python3.5

# Program to implement Ceasar Cipher encryption and decryption.

from textconverter import *


class CipherExceptions(Exception):
    def __init__(self, msg):
        super(CipherExceptions, self).__init__(msg)


class CeasarCipher:
    def __init__(self, key):
        self.__key = key
        self.__encrypt = dict()
        self.__decrypt = dict()
        self.gen_dict()

    def gen_dict(self):
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        start = ord('a') - key

        for i in range(0, len(alphabets) - key):
            ch = alphabets[i]
            self.__encrypt[ch] = chr(ord(ch) + key)
            self.__decrypt[chr(ord(ch) + key)] = ch

        for i in range(len(alphabets) - key, len(alphabets)):
            ch = alphabets[i]
            self.__encrypt[ch] = chr(start + key)
            self.__decrypt[chr(start + key)] = ch
            start += 1
        return

    def get_encrypted_char(self, char):
        return self.__encrypt[char]

    def get_decrypted_char(self, char):
        return self.__decrypt[char]

    def encrypt(self, plain):
        cipher = ''
        for ch in get_alphabetic_msg(plain):
            cipher += self.get_encrypted_char(ch)
        return get_msg_with_punctuations(plain, cipher)

    def decrypt(self, cipher):
        plain = ''
        for ch in get_alphabetic_msg(cipher):
            plain += self.get_decrypted_char(ch)
        return get_msg_with_punctuations(cipher, plain)


def choices():
    print('\nOptions')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Exit')
    print('\nEnter your choice: ', end='')
    choice = int(input())
    return choice


def input_key():
    while True:
        try:
            print('\nEnter a key: ', end='')
            key = int(input())
            if key > 26:
                raise CipherExceptions('Invalid key length.')
            else:
                return key
        except Exception as e:
            print(e, end=' ')
            print("Let's try again!")

if __name__=='__main__':
    while True:
        try:
            choice = choices()
            if choice == 1:
                key = input_key()
                ceasar_cipher = CeasarCipher(key)
                print('\nEnter message to be encrypted : ', end='')
                ptext = str(input())
                print('The encrypted text is : ', ceasar_cipher.encrypt(ptext))
            elif choice == 2:
                key = input_key()
                ceasar_cipher = CeasarCipher(key)
                print('\nEnter message to be decrypted : ', end='')
                ctext = str(input())
                print('The decrypted text is : ', ceasar_cipher.decrypt(ctext))
            elif choice == 3:
                print('\n*** Goodbye! ***')
                break
            else:
                raise CipherExceptions('Invalid choice.')
        except ValueError as e:
            print('Invalid input', end=' ')
            print("Let's try again!")
        except CipherExceptions as e:
            print(e, end=' ')
            print("Let's try again!")
