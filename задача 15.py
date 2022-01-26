for A in range(0, 1000):
    flag = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not(((x * y) < A) or (x < y) or (x >= 12)):
                flag = 0

    if flag:
        print(A)
