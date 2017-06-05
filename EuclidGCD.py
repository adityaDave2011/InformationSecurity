# /bin/python3.5

from math import fabs


class CipherExceptions(Exception):
    def __init__(self, msg):
        super(CipherExceptions, self).__init__(msg)


def gcd_by_euclid(a, b):
    if a < 0 or b < 0:
        a = fabs(a)
        b = fabs(b)
    if b == 0:
        return int(a)
    if b > a:
        gcd_by_euclid(b, a)
    return gcd_by_euclid(b, a % b)


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


def main():
    a = input_num('Enter first number : ')
    b = input_num('Enter second number : ')
    print('\nThe GCD of {} and {} is {}'.format(a, b, gcd_by_euclid(a, b)))

if __name__ == '__main__':
    main()
