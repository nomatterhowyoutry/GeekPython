# 2. Write a script to print out a set containing all the colours
#     from color_list_1 which are not present in color_list_2. 
#         Test Data : 
#         color_list_1 = set(["White", "Black", "Red"]) 
#         color_list_2 = set(["Red", "Green"])
#         Expected Output : 
#         {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_list_3 = []

for i in color_list_1:
    if i not in color_list_2:
        color_list_3.append(i)

print(set(color_list_3))