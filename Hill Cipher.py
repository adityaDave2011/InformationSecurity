#!/usr/bin/python3.5

# Program to implement Hill Cipher encryption and decryption.

from math import ceil

import numpy as np
from algorithms import matrix_inv
from textconverter import *


class CipherExceptions(Exception):
    def __init__(self, msg):
        super(CipherExceptions, self).__init__(msg)


class HillCipher:
    def __init__(self, key_size, key):
        self.__key = key
        self.__key_size = key_size
        self.__encrypt = dict()
        self.__decrypt = dict()
        self.__map_to_num = dict()
        self.__map_to_alpha = dict()
        self.gen_dict()
        self.__key_inv = matrix_inv(self.__key)

    def gen_dict(self):
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(alphabets)):
            self.__map_to_num[alphabets[i]] = i
            self.__map_to_alpha[i] = alphabets[i]
        return

    def gen_grams(self, text):
        gram_list = list()
        no_of_grams = ceil(len(text) / self.__key_size)
        for i in range(no_of_grams):
            gram_list.append(text[key_size * i:key_size * i + key_size])
        return gram_list

    def map_to_num(self, string):
        list_str = list(string)
        mapped = list()
        for char in list_str:
            mapped.append(self.__map_to_num[char])
        return mapped

    def map_to_alpha(self, gram):
        mapped = list()
        for num in gram:
            mapped.append(self.__map_to_alpha[num])
        return mapped

    def get_encrypted_gram(self, gram):
        cipher = np.dot(gram, self.__key)
        return np.mod(cipher, 26)

    def get_decrypted_gram(self, gram):
        plain = np.dot(gram, self.__key_inv)
        return np.mod(plain, 26)

    def encrypt(self, plain):
        cipher_grams = list()
        gram_list = self.gen_grams(self.map_to_num(get_alphabetic_msg(plain)))
        for gram in gram_list:
            cipher_grams.append(self.map_to_alpha(self.get_encrypted_gram(gram).tolist()))
        return ''.join(''.join(gram) for gram in get_msg_with_punctuations(plain, cipher_grams))

    def decrypt(self, cipher):
        plain_grams = list()
        gram_list = self.gen_grams(self.map_to_num(get_alphabetic_msg(cipher)))
        for gram in gram_list:
            plain_grams.append(self.map_to_alpha(self.get_decrypted_gram(gram)))
        return ''.join(''.join(gram) for gram in get_msg_with_punctuations(cipher, plain_grams))


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
            print('\nEnter size of key: ', end='')
            size_of_key = int(input())
            if size_of_key > 26:
                raise CipherExceptions('Invalid key length.')
            else:
                key = list()
                for i in range(size_of_key):
                    print('\nEnter the {0} row (separate numbers with spaces): '.format(i+1), end='')
                    row = str(input()).strip()
                    key.append([int(s) for s in row.split(' ')])
                return size_of_key, key
        except Exception as e:
            print(e, end=' ')
            print("Let's try again!")


if __name__ == '__main__':
    while True:
        try:
            choice = choices()
            if choice == 1:
                key_size, key = input_key()
                hill_cipher = HillCipher(key_size, key)
                print('\nEnter message to be encrypted : ', end='')
                ptext = str(input())
                print('The encrypted text is : ', hill_cipher.encrypt(ptext))
            elif choice == 2:
                key_size, key = input_key()
                hill_cipher = HillCipher(key_size, key)
                print('\nEnter message to be decrypted : ', end='')
                ctext = str(input())
                print('The decrypted text is : ', hill_cipher.decrypt(ctext))
            elif choice == 3:
                print('\n*** Goodbye! ***')
                break
            else:
                raise CipherExceptions('Invalid choice.')
        except ValueError as e:
            print('Invalid input', e, end=' ')
            print("Let's try again!")
        except CipherExceptions as e:
            print(e, end=' ')
            print("Let's try again!")
