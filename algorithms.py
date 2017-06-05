# /bin/python3.5

from math import fabs
from sympy import Matrix
from math import gcd
from numpy.linalg import det


def euler_totient(n):
    count = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            count += 1
    return count


def gcd_by_euclid(a, b):
    if a < 0 or b < 0:
        a = fabs(a)
        b = fabs(b)
    if b == 0:
        return int(a)
    if b > a:
        gcd_by_euclid(b, a)
    return gcd_by_euclid(b, a % b)


def matrix_inv(key):
    try:
        detr = det(key)
        mod_inv = mod_inverse(detr % 26, 26)
        adjoint = Matrix(key).adjugate()
        adjoint = adjoint.tolist()
        inv_mat = [[int(col * mod_inv) for col in row] for row in adjoint]
        mod_mat = [[col % 26 for col in row] for row in inv_mat]
        return mod_mat
    except Exception as e:
        print(e)


def extended_euclid_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_euclid_algorithm(b % a, a)
        return g, x - (b // a) * y, y


def mod_inverse(a, m):
    g, x, y = extended_euclid_algorithm(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def main():
    print(extended_euclid_algorithm(3, 11))

if __name__ == '__main__':
    main()
