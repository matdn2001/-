def F(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            first = i
            second = x // first
            if first != second:
                return second - first
    return 0


k = 0
number = 700001
while k != 6:
    f = F(number)
    if f != 0 and f % 7 == 0:
        k += 1
        print(number, f)
    number += 1