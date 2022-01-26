f = open("26.txt", "r")
S, N = map(int, f.readline().strip().split())
array = []
for size in f:
    array.append(int(size))
f.close()

array.sort()

max_size = 0
max_count = 0

i = 0

while max_size < S and i < N:
    max_size += array[i]
    max_count += 1
    i += 1

if max_size > S:
    i -= 1
    max_count -= 1
    max_size -= array[i]
    max_size -= array[i - 1]

    difference = S - max_size

    while array[i] <= difference and i < N:
        i += 1
    i -= 1
    max_size += array[i]

print(max_count, array[i])
