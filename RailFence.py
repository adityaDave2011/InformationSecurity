#!/usr/bin/python3.5

# Program to implement Rail Fence Cipher encryption and decryption.

from math import ceil

from textconverter import *


class CipherExceptions(Exception):
    def __init__(self, msg):
        super(CipherExceptions, self).__init__(msg)


class RailFenceCipher:
    def __init__(self, key):
        self.__depth = key
        self.__matrix = None

    def init_matrix_encrypt(self, plain):
        cols = ceil(len(plain) // self.__depth)
        self.__matrix = list()
        for i in range(0, self.__depth):
            self.__matrix.append(list())
            for j in range(0, cols + 1):
                try:
                    self.__matrix[i].append(plain[i + j * self.__depth])
                except IndexError:
                    pass

    def init_matrix_decrypt(self, cipher):
        cols = ceil(len(cipher) // self.__depth)
        self.__matrix = list()
        start = 0
        for i in range(0, self.__depth):
            try:
                self.__matrix.append(list(cipher[start:start + cols + 1]))
                start = cols + 1
            except IndexError:
                pass

    def encrypt(self, plain):
        cipher = ''
        self.init_matrix_encrypt(get_alphabetic_msg(plain))
        for sub_list in self.__matrix:
            cipher += ''.join(sub_list)
        return get_msg_with_punctuations(plain, cipher)

    def decrypt(self, cipher):
        plain = ''
        self.init_matrix_decrypt(get_alphabetic_msg(cipher))
        for j in range(0, ceil(len(cipher) // self.__depth) + 1):
            for i in range(0, self.__depth):
                try:
                    plain += self.__matrix[i][j]
                except IndexError:
                    pass
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
    print('\nEnter a depth: ', end='')
    key = int(input())
    return key

if __name__ == '__main__':
    while True:
        try:
            choice = choices()
            if choice == 1:
                key = input_key()
                print('\nEnter message to be encrypted : ', end='')
                ptext = str(input())
                rail_fence_cipher = RailFenceCipher(key)
                print('The encrypted text is : ', rail_fence_cipher.encrypt(ptext))
            elif choice == 2:
                key = input_key()
                print('\nEnter message to be decrypted : ', end='')
                ctext = str(input())
                rail_fence_cipher = RailFenceCipher(key)
                print('The decrypted text is : ', rail_fence_cipher.decrypt(ctext))
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
