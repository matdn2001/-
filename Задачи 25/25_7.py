def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def list_of_divisors(x):
    A = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            first = i
            second = x // first
            A.append(first)
            if first != second:
                A.append(second)
    return sorted(A)


k = 0
number = 200001
while k != 6:
    A = list_of_divisors(number)
    if len(A) != 0 and isPrime(A[-1] and isPrime(A[-2])):
        k += 1
        print(A[-1], A[-2])
    number += 1