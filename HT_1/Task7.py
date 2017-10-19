# 7. Write a script to concatenate all elements in a list into a string and print it.

list = [i for i in range(0, 10)]
print(''.join(str(i) for i in list))