#!/usr/bin/python3.5

# Program to implement RSA (Riverset-Shamir-Adleman) and decryption.

from algorithms import euler_totient
from algorithms import mod_inverse
from textconverter import *


class CipherExceptions(Exception):
    def __init__(self, msg):
        super(CipherExceptions, self).__init__(msg)


class RSACipher:
    def __init__(self, p_prime, q_prime, e_prime, block_size):
        self.__p = p_prime
        self.__q = q_prime
        self.block_size = block_size
        self.n = p_prime * q_prime
        self.e = e_prime
        self.__map_alpha_to_num = dict()
        self.__map_num_to_alpha = dict()
        self.__d = mod_inverse(self.e, euler_totient(self.n))
        self.init_mappings()

    def init_mappings(self):
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        cap_alphabets = alphabets.upper()
        length = len(alphabets)
        for i in range(0, length):
            self.__map_alpha_to_num[alphabets[i]] = str(i)
            self.__map_num_to_alpha[str(i)] = alphabets[i]
        for i in range(length, 2*length):
            self.__map_alpha_to_num[cap_alphabets[i - length]] = str(i)
            self.__map_num_to_alpha[str(i)] = cap_alphabets[i - length]

    def get_encrypted_block(self, block):
        num_repr = 0
        print('in block : ', block)
        for char in block:
            num_repr = num_repr*100 + int(self.__map_alpha_to_num.get(char))
        encrypt_block = (num_repr ** self.e) % self.n
        return encrypt_block

    def get_decrypted_block(self, block):
        decrypt_block = str((int(block) ** self.__d) % self.n)
        length = len(decrypt_block)
        if length is block_size:
            return decrypt_block
        else:
            return decrypt_block.zfill(self.block_size)

    def encrypt(self, plain):
        cipher = ''
        blocks = gen_blocks(get_alphabetic_msg(plain), self.block_size)
        for block in blocks:
            cipher += str(self.get_encrypted_block(block)) + ' '
        cipher = cipher.strip()
        return cipher

    def decrypt(self, cipher):
        plain = list()
        no_of_chars = (block_size // 2)
        blocks = cipher.split()
        for block in blocks:
            plain.append(self.get_decrypted_block(block))
        chars = ''
        for block in plain:
            for i in range(0, no_of_chars):
                ch = block[i * no_of_chars: i * no_of_chars + 2]
                if ch == '00':
                    ch = '0'
                chars += self.__map_num_to_alpha.get(ch)
        return chars


def gen_blocks(text, block_size):
    no_of_chars = (block_size // 2)
    no_of_blocks = len(text) // no_of_chars
    blocks = list()
    for i in range(0, no_of_blocks):
        blocks.append(text[no_of_chars * i:no_of_chars * i + no_of_chars])
    if isinstance(len(text) // (block_size // 2), float):
        blocks.append(text[no_of_blocks * block_size:])
    return blocks


def choices():
    print('\nOptions')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Exit')
    print('\nEnter your choice: ', end='')
    return int(input())


def input_num(message):
    while True:
        try:
            print('\n', message, end='')
            key = str(input())
            if not str.isnumeric(key):
                raise CipherExceptions('Please enter a proper number.')
            else:
                return int(key)
        except Exception as e:
            print(e, end=' ')
            print("Let's try again!")


if __name__ == '__main__':
    while True:
        try:
            choice = choices()
            if choice == 3:
                print('\n*** Goodbye! ***')
                exit(0)
            if choice >= 4:
                raise CipherExceptions('Invalid choice.')
            p_prime = input_num('Enter first prime number : ')
            q_prime = input_num('Enter second prime number : ')
            e_prime = input_num('Enter value of e : ')
            block_size = input_num('Enter the block size (number of decimal digits): ')
            rsa_cipher = RSACipher(p_prime, q_prime, e_prime, block_size)
            if choice == 1:
                message = str(input('\nEnter message to be encrypted : '))
                print('\nThe encrypted text is : ', rsa_cipher.encrypt(message))
            elif choice == 2:
                message = str(input('\nEnter message to be decrypted (blocks separated by spaces): '))
                print('\nThe decrypted text is : ', rsa_cipher.decrypt(message))
        except CipherExceptions as e:
            print(e, end=' ')
            print("Let's try again!")
