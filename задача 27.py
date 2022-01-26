f = open("27_A.txt", "r")
N = int(f.readline().strip())
del_2 = 0
del_13 = 0
del_26 = 0
for number in f:
    number = int(number)
    if number % 26 == 0:
        del_26 += 1
    elif number % 2 == 0:
        del_2 += 1
    elif number % 13 == 0:
        del_13 += 1
f.close()
count = 0
if del_13 != 0 and del_2 != 0:
    count = del_13 * del_2
count += del_26 * (N - del_26)
count += del_26 * (del_26 - 1) / 2
print(count)