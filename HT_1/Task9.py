#9. Write a script to remove an empty tuple(s) from a list of tuples.

List = [(1), (), (''), (1, 2, 3), ("", 3)]
for i in List:
    if not i:
        List.remove(i)
print(List)