def M(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            first = i
            second = x // first
            return first + second
    return 0


k = 0
number = 250671
while k != 6:
    m = M(number)
    if m != 0 and m % 7 == 4:
        k += 1
        print(number, m)
    number += 1