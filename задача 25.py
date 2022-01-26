def count_del(n):
    count_d = 2
    for delit in range(2, n):
        if n % delit == 0:
            count_d += 1
    return count_d


max_count = 0
max_number = 0
for i in range(120115, 120200 + 1):
    count = count_del(i)
    if count >= max_count:
        max_number = i
        max_count = count
print(max_count, max_number)
