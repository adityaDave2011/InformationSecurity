#!/usr/bin/python3.5

# Program to implement Monoalphabetic Cipher encryption and decryption.


from textconverter import *

class CipherExceptions(Exception):
    def __init__(self, msg):
        super(CipherExceptions, self).__init__(msg)


class MonoalphabeticCipher:
    def __init__(self, key):
        self.__key = key
        self.__encrypt = dict()
        self.__decrypt = dict()
        self.gen_dict()

    def gen_dict(self):
        alphabets = 'abcdefghijklmnopqrstuvwxyz'

        for i in range(0, 26):
            self.__encrypt[alphabets[i]] = key[i]
            self.__decrypt[key[i]] = alphabets[i]
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
            key = str(input())
            if len(key) != 26:
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
                monoalphabeticCipher = MonoalphabeticCipher(key)
                print('\nEnter message to be encrypted : ', end='')
                ptext = str(input())
                print('The encrypted text is : ', monoalphabeticCipher.encrypt(ptext))
            elif choice == 2:
                key = input_key()
                monoalphabeticCipher = MonoalphabeticCipher(key)
                print('\nEnter message to be decrypted : ', end='')
                ctext = str(input())
                print('The decrypted text is : ', monoalphabeticCipher.decrypt(ctext))
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
