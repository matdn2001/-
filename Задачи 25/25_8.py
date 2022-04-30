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


for i in range(200123, 200150 + 1):
    A = list_of_divisors(i)
    if len(A) == 4:
        print(A)
