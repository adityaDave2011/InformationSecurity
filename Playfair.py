#!/usr/bin/python3.5

# Program to implement Playfair Cipher encryption and decryption.

from collections import OrderedDict
from math import ceil

from textconverter import *


class CipherExceptions(Exception):
    def __init__(self, msg):
        super(CipherExceptions, self).__init__(msg)


class PlayfairCipher:
    def __init__(self, key):
        self.__key = key
        self.__encrypt = dict()
        self.__decrypt = dict()
        self.__matrix = [[0]*5 for i in range(5)]
        self.gen_matrix()

    def gen_matrix(self):
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        self.__key += alphabets
        self.__key = list(OrderedDict.fromkeys(self.__key))
        ijcame = False

        i, j = 0, 0
        while i <= 4:
            j = 0
            while j <= 4:
                char = self.__key.pop(0)
                if (char is 'i' or char is 'j') and not ijcame:
                    self.__matrix[i][j] = 'ij'
                    ijcame = True
                    j += 1
                elif (char is 'i' or char is 'j') and ijcame:
                    continue
                else:
                    self.__matrix[i][j] = char
                    j += 1
            i += 1
        print('\nThe PlayFair matrix is...')
        for row in self.__matrix:
            print(row)
        return

    def gen_digrams(self, text):
        digram_list = list()
        no_of_digrams = ceil(len(text) / 2)
        for i in range(no_of_digrams):
            digram = text[2 * i:2 * i + 2]
            if (len(digram) is 2) and (digram[0] is digram[1]):
                text = text[0:2 * i + 1] + 'x' + text[2 * i + 1:len(text)]
        for i in range(no_of_digrams):
            digram = text[2 * i:2 * i + 2]
            digram_list.append(digram)
        return digram_list

    def find_digram_pos(self, digram):
        x, y, p, q, i, j = 0, 0, 0, 0, 0, 0
        for i in range(5):
            for j in range(5):
                if (digram[0] is 'i' or digram[0] is 'j') and (self.__matrix[i][j] is 'ij'):
                    x, y = i, j
                elif (digram[1] is 'i' or digram[1] is 'j') and (self.__matrix[i][j] is 'ij'):
                    p, q = i, j
                elif digram[0] is self.__matrix[i][j]:
                    x, y = i, j
                elif digram[1] is self.__matrix[i][j]:
                    p, q = i, j
        return x, y, p, q

    def get_new_char(self, x, y):
        char = self.__matrix[x % 5][y % 5]
        if char is 'ij':
            return 'i'
        return char

    def get_encrypted_digram(self, p_digram):
        x, y, p, q = self.find_digram_pos(str.lower(p_digram))

        # characters in same row
        if x == p:
            c_digram = self.get_new_char(x, y + 1) + self.get_new_char(p, q + 1)

        # characters in same column
        elif y == q:
            c_digram = self.get_new_char(x + 1, y) + self.get_new_char(p + 1, q)

        # characters in different rows and columns
        else:
            c_digram = self.get_new_char(x, q) + self.get_new_char(p, y)

        return c_digram

    def get_decrypted_digram(self, c_digram):
        x, y, p, q = self.find_digram_pos(str.lower(c_digram))

        # characters in same row
        if x == p:
            p_digram = self.get_new_char(x, y - 1) + self.get_new_char(p, q - 1)

        # characters in same column
        elif y == q:
            p_digram = self.get_new_char(x - 1, y) + self.get_new_char(p - 1, q)

        # characters in different rows and columns
        else:
            p_digram = self.get_new_char(x, q) + self.get_new_char(p, y)

        return p_digram

    def encrypt(self, plain):
        cipher = ''
        digram_list = self.gen_digrams(get_alphabetic_msg(plain))
        for digram in digram_list:
            cipher += self.get_encrypted_digram(digram)
        return get_msg_with_punctuations(plain, cipher)

    def decrypt(self, cipher):
        plain = ''
        digram_list = self.gen_digrams(get_alphabetic_msg(cipher))
        for digram in digram_list:
            plain += self.get_decrypted_digram(digram)
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
            if any((char.isdigit() or char == ' ') for char in key):
                raise CipherExceptions('Key contains non-alphabetic characters.')
            else:
                return key
        except Exception as e:
            print(e, end=' ')
            print("Let's try again!")

if __name__ == '__main__':
    while True:
        try:
            choice = choices()
            if choice == 1:
                key = input_key()
                playfairCipher = PlayfairCipher(key)
                print('\nEnter message to be encrypted : ', end='')
                ptext = str(input())
                print('The encrypted text is : ', playfairCipher.encrypt(ptext))
            elif choice == 2:
                key = input_key()
                playfairCipher = PlayfairCipher(key)
                print('\nEnter message to be decrypted : ', end='')
                ctext = str(input())
                print('The decrypted text is : ', playfairCipher.decrypt(ctext))
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
