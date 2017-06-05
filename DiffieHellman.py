#!/usr/bin/python3.5

# Program to implement Diffie Hellman Key Exchange Algorithm.


class CipherExceptions(Exception):
    def __init__(self, msg):
        super(CipherExceptions, self).__init__(msg)


class DiffieHellman:
    @staticmethod
    def calc_public_key(primitive_root, prime_num, private_key):
        return (primitive_root ** private_key) % prime_num

    @staticmethod
    def calc_true_key(private_key, prime_num, partner_public_key):
        return (partner_public_key ** private_key) % prime_num


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
    q_prime = input_num('Enter a large prime number : ')
    primitive_root = input_num('Enter the primitive root : ')
    a_private_key = input_num('Enter A\'s private key : ')
    b_private_key = input_num('Enter B\'s private key : ')
    print('\n*****Summary*****\n')
    a_public_key = DiffieHellman.calc_public_key(primitive_root, q_prime, a_private_key)
    b_public_key = DiffieHellman.calc_public_key(primitive_root, q_prime, b_private_key)
    print('A\'s public key : ', a_public_key)
    print('B\'s public key : ', b_public_key)
    a_main_key = DiffieHellman.calc_true_key(a_private_key, q_prime, b_public_key)
    b_main_key = DiffieHellman.calc_true_key(b_private_key, q_prime, a_public_key)
    print('Original key : ', a_main_key)

