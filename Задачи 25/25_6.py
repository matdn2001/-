def sum_of_divisors(x):
    s = 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            first = i
            second = x // first
            s += first
            if first != second:
                s += second
    return s


k = 0
number = 550001
while k != 6:
    s = sum_of_divisors(number)
    if s % 3 != 0 and s % 5 == 0:
        k += 1
        print(number, s // 8)
    number += 1