for n in range(3, 30):
    for x in range(1, n):
        for y in range(0, n):
            for z in range(0, n):
                if x * n**2 + y * n + z == 30:
                    print(n)
                    print(str(x) + str(y) + str(z))
