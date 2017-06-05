# /usr/bin/python

from math import ceil
from math import fmod
from math import gcd
import numpy as np
from numpy.linalg import inv
from numpy.linalg import det


def gen_digrams(text):
    digram_list = list()
    no_of_digrams = ceil(len(text) / 2)
    for i in range(no_of_digrams):
        digram = text[2 * i:2 * i + 2]
        digram_list.append(digram)
    print(digram_list)
    return


def gen_safe_digrams2(text):
    digram_list = list()
    no_of_digrams = ceil(len(text) / 2)
    for i in range(no_of_digrams):
        digram = text[2 * i:2 * i + 2]
        if (len(digram) is 2) and (digram[0] is digram[1]):
            text = text[0:2 * i + 1] + 'x' + text[2 * i + 1:len(text)]
    for i in range(no_of_digrams):
        digram = text[2 * i:2 * i + 2]
        digram_list.append(digram)
    print(digram_list)
    return


def get_alphabetic_msg(text):
    alpha_text = ''
    for char in text:
        if str.isalpha(char):
            alpha_text += char
    return alpha_text


def retrieve_grammar(old, new):
    new_org_text = new
    for i in range(len(old)):
        if not str.isalpha(old[i]):
            new_org_text = new_org_text[0:i] + old[i] + new_org_text[i:]
    return new_org_text


def input_key():
    while True:
        try:
            print('\nEnter size of key: ', end='')
            size_of_key = int(input())
            if size_of_key > 26:
                raise Exception('Invalid key length.')
            else:
                key = list()
                for i in range(size_of_key):
                    print('\nEnter the {0} row (separate numbers with spaces): '.format(i+1), end='')
                    row = str(input())
                    key.append([int(s) for s in row.split(' ')])
                return key
        except Exception as e:
            print(e, end=' ')
            print("Let's try again!")


def generalized_euclidian_algorithm(a, b):
    if b > a:
        return generalized_euclidian_algorithm(b,a);
    elif b == 0:
        return 1, 0
    else:
        (x, y) = generalized_euclidian_algorithm(b, a % b);
        return y, x - (a / b) * y


def mod_inverse_naive(a, p, r):
    if gcd(a, p) != 1:
        return -1
    for i in range(0, p):
        if r == (a * i) % p:
            return i


def mod_inverse_euclid(a, p):
    if gcd(a, p) != 1:
        return -1





def main():
    # gen_digrams("keywords")
    # gen_safe_digrams2("balloon")
    # gen_safe_digrams2("engineering")
    # gen_safe_digrams2("let's go!")
    # al = get_alphabetic_msg("let's go")
    # print(al)
    # print(retrieve_grammar("let's go", al))
    # input_key()
    # arr = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
    # print(arr)
    # inverse = inv(arr)
    # print(inverse)
    # deter = det(arr)
    # print(fmod(deter, 26))
    # print(generalized_euclidian_algorithm(121, 26))
    print(mod_inverse_naive(3, 11, 1))

    print(modinv(3, 11))

if __name__ == '__main__':
    main()