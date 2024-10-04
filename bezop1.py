from random import randint
import math


def find_d(e_, phi_):
    d_ = 1
    for i in range(2, 99999):
        if (i * e_) % phi_ == 1 and i != e_:
            d_ = i
            break
    return d_


def check(a):
    k = 0
    fl = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k = k + 1
    if k <= 0:
        fl = 1
    return fl


print('Input p and q')
p, q = [int(_) for _ in input().split()]

if not check(p) or not check(q):
    print('Wrong, input simple num')
    p, q = [int(_) for _ in input().split()]

n = p * q
print(f'N = {n}')

phi = (p-1) * (q-1)
print(f'phi = {phi}')

e = randint(2, phi-1)
while not (math.gcd(e, phi) == 1):
    print(e)
    e = randint(2, phi-1)

print(f'\ne = {e}')

d = find_d(e, phi)
print(f'd = {d}')
print(f'\nOpen key - ({e}, {n}), Closed key - ({d}, {n}) ')

print('\nInput your num to encrypt')
inp = int(input())
while inp >= n:
    print(f'\nWrong, input num < {n}')
    inp = int(input())

print('\nEncryption...')

ans = pow(inp, e, n)

print(f'\nYour encrypt message {ans}\n')




