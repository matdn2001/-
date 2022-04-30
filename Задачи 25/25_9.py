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


print(13456 ** 0.5, 201654 ** 0.5)  # 116.0; 449.0590161660269
for i in range(116, 449 + 1):
    x = i ** 2
    A = list_of_divisors(x)
    if len(A) == 7:
        print(A)
