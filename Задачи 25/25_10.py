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


print(223344556 ** 0.5, 323456789 ** 0.5)  # 14944.716658404735; 17984.904475698502
for i in range(14945, 17984 + 1):
    x = i ** 2
    A = list_of_divisors(x)
    if len(A) == 3:
        print(x, A[-1])
