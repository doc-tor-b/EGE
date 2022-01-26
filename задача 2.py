print("x w z y")
for x in 1, 0:
    for y in 1, 0:
        for w in 1, 0:
            for z in 1, 0:
                if not((x and not(y)) or (x == z) or not(w)):
                    print(x, w, z, y)