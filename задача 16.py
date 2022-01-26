def F(n):
    if n == 1: return 1
    if (n >= 2):
        return F(n - 1) - G(n - 1)


def G(n):
    if n == 1: return 1
    if (n >= 2):
        return F(n - 1) + G(n - 1)


print(F(5) / G(5))
