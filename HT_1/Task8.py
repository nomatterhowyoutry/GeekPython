# 8. Write a script to replace last value of tuples in a list. 
#         Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#         Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

List = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

List = [list(List[i]) for i in range(0, len(List))]
for i in range(0, len(List)):
    List[i][-1] = 100
    List[i] = tuple(List[i])
    
print(List)