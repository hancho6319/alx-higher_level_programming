#!/usr/bin/python3

list1 = [[2, 4, 7, 1], [3, 1, 1, 0], [10, 6, 11, 15]]
list2 = []

list2 = list1.copy()

for ele in range(len(list1)):
    list2[ele] = list(map(lambda x: x**2, list1[ele]))

print(f"The list1 elements are {list1}")
print(f"The list2 elements are {list2}")
