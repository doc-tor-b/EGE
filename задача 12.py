string = "1" * 98
while string.find("1111") != -1:
    string = string.replace("1111", "22", 1)
    string = string.replace("222", "1", 1)

print(string)