f = open("24.txt", "r")
string = f.read().strip()
end = len(string)
i = 2
array = [0] * (ord('Z') + 1)
while i < end:
    if string[i - 2] == string[i - 1]:
        array[ord(string[i])] += 1
    i += 1
max_symb = 0
max_count = 0
f.close()

for i in range(ord('A'), ord('Z') + 1):
    if max_count < array[i]:
        max_count = array[i]
        max_symb = i

print(chr(max_symb))