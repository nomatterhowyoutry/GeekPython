# 6. Write a script to check whether a specified value is contained in a group of values. 
#         Test Data : 
#         3 -> [1, 5, 8, 3] : True
#         -1 -> (1, 5, 8, 3) : False

list = [1, 5, 8, 3]
tuple = tuple(list)

print(3 in list)
print(-1 in tuple)