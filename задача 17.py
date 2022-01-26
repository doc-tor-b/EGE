# Слишком умный способ подходит больше для 27 задачи с похожим условием

f = open("17.txt", "r")
array = [0] * 126
max_array = [0] * 127

for number in f:
    n = int(number)
    array[n % 126] += 1
    if n % 126 == 0:
        if n >= max_array[0]:
            max_array[126] = max_array[0]
            max_array[0] = n
    elif max_array[n % 126] < n:
        max_array[n % 126] = n

f.close()

count = 0
for i in range(1, 126 // 2):
    if array[i] != 0 and array[126 - i] != 0:
        local_count = array[i] * array[126 - i]
        count += local_count

if array[0] > 0:
    count += array[0] * (array[0] - 1) / 2

if array[63] != 0:
    count += array[63] * (array[63] - 1) / 2
max_sum = 0

for i in range(1, 126):
    if max_array[i] != 0 and max_array[126 - i] != 0 and max_array[i] + max_array[126 - i] > max_sum:
        max_sum = max_array[i] + max_array[126 - i]

if max_array[0] != 0 and max_array[126] != 0:
    max_sum = max(max_sum, max_array[0] + max_array[126])

print("count", count)
print("max_sum", max_sum)
