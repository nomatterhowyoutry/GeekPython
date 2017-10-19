# 11. Write a script to remove duplicates from Dictionary.

dic = {1: 10, 2:10, 3:8, 4:5, 5:17, 6:5}

result = dict()
for key,value in dic.items():
    if value not in result.values():
        result[key] = value
print(result)