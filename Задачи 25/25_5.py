def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def S(x):
    s = 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            first = i
            second = x // first
            if isPrime(first):
                s += first
            if isPrime(second) and first != second:
                s += second
    return s


k = 0
number = 450001
while k != 6:
    s = S(number)
    if s != 0 and s % 7 == 0:
        k += 1
        print(number, s)
    number += 1