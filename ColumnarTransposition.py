#!/usr/bin/python3.5

# Program to implement Column Transposition Cipher encryption and decryption.

from math import ceil

from textconverter import *


class CipherExceptions(Exception):
    def __init__(self, msg):
        super(CipherExceptions, self).__init__(msg)


class ColumnTranspositionCipher:
    def __init__(self, key):
        self.__key = key
        self.__cols = max(self.__key) + 1
        self.__matrix = list()

    def init_matrix_encrypt(self, plain):
        no_of_rows = ceil(len(plain) // self.__cols)
        start = 0
        for i in range(0, no_of_rows):
            try:
                self.__matrix.append(list(plain[start:start + self.__cols]))
                start += self.__cols
            except IndexError:
                print(e)
                pass

    def init_matrix_decrypt(self, cipher):
        no_of_rows = ceil(len(cipher) // self.__cols)
        self.__matrix = [['0']*self.__cols for _ in range(0, no_of_rows)]
        cipher = list(cipher)
        for i in range(0, self.__cols):
            col = self.__key.index(i)
            for i in range(0, no_of_rows):
                self.__matrix[i][col] = cipher.pop(0)

    def encrypt(self, plain):
        cipher = ''
        self.init_matrix_encrypt(get_alphabetic_msg(plain))
        for i in range(self.__cols):
            col = self.__key.index(i)
            for row in self.__matrix:
                cipher += row[col]
        return get_msg_with_punctuations(plain, cipher)

    def decrypt(self, cipher):
        plain = ''
        self.init_matrix_decrypt(get_alphabetic_msg(cipher))
        for row in self.__matrix:
            plain += ''.join(row)
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
    print('\nEnter a key (digits separated by spaces): ', end='')
    key = [(int(num) - 1) for num in str(input()).split()]
    return key

if __name__ == '__main__':
    while True:
        try:
            choice = choices()
            if choice == 1:
                key = input_key()
                print('\nEnter message to be encrypted : ', end='')
                ptext = str(input())
                column_transposition_cipher = ColumnTranspositionCipher(key)
                print('The encrypted text is : ', column_transposition_cipher.encrypt(ptext))
            elif choice == 2:
                key = input_key()
                print('\nEnter message to be decrypted : ', end='')
                ctext = str(input())
                column_transposition_cipher = ColumnTranspositionCipher(key)
                print('The decrypted text is : ', column_transposition_cipher.decrypt(ctext))
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
