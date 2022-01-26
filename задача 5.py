def f(n):
    n = bin(n)[2:]
    last = len(n)
    n += n[last - 1]
    n += str(n.count("1") % 2)
    return int(n, 2)


for i in range(1, 100):
    val = f(i)
    if val > 105:
        print(val)
