def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def P(x):
    p = 1
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            first = i
            second = x // first
            if not isPrime(first):
                p *= first
            if not isPrime(second) and first != second:
                p *= second
    return p


k = 0
number = 101
while k != 7:
    p = P(number)
    if p % 10 == 8:
        k += 1
        print(number, p)
    number += 1