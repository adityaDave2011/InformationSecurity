#!/usr/bin/python3.5

# Program to implement Monoalphabetic Cipher encryption and decryption.

from textconverter import *


alphabets = 'abcdefghijklmnopqrstuvwxyz'


class CipherExceptions(Exception):
    def __init__(self, msg):
        super(CipherExceptions, self).__init__(msg)


class VigenereCipher:
    def __init__(self, keyword, text):
        self.__key = str(keyword).lower()
        self.gen_dict(get_alphabetic_msg(text))

    def gen_dict(self, text):
        if len(self.__key) < len(text):
            times = len(text) // len(self.__key)
            remaining = len(text) % len(self.__key)
            self.__key = times * self.__key + self.__key[0:remaining]
        return

    def get_encrypted_char(self, key_char, pchar):
        return alphabets[(alphabets.find(key_char) + alphabets.find(pchar)) % 26]

    def get_decrypted_char(self, key_char, cchar):
        return alphabets[(alphabets.find(cchar) - alphabets.find(key_char)) % 26]

    def encrypt(self, plain):
        cipher = ''
        plain_norm = get_alphabetic_msg(plain)
        for i in range(0, len(plain_norm)):
            cipher += self.get_encrypted_char(self.__key[i], plain_norm[i])
        return get_msg_with_punctuations(plain, cipher)

    def decrypt(self, cipher):
        plain = ''
        cipher_norm = get_alphabetic_msg(cipher)
        for i in range(0, len(cipher_norm)):
            plain += self.get_decrypted_char(self.__key[i], cipher_norm[i])
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
    print('\nEnter a keyword: ', end='')
    key = str(input())
    return key

if __name__=='__main__':
    while True:
        try:
            choice = choices()
            if choice == 1:
                keyword = input_key()
                print('\nEnter message to be encrypted : ', end='')
                ptext = str(input())
                vigenereCipher = VigenereCipher(keyword, ptext)
                print('The encrypted text is : ', vigenereCipher.encrypt(ptext))
            elif choice == 2:
                key = input_key()
                print('\nEnter message to be decrypted : ', end='')
                ctext = str(input())
                vigenereCipher = VigenereCipher(keyword, ctext)
                print('The decrypted text is : ', vigenereCipher.decrypt(ctext))
            elif choice == 3:
                print('\n*** Goodbye! ***')
                break
            else:
                raise CipherExceptions('Invalid choice')
        except ValueError as e:
            print('Invalid input', end=' ')
            print("Let's try again!")
        except CipherExceptions as e:
            print(e, end=' ')
            print("Let's try again!")
