#!/usr/bin/python3

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }

list1 = list(a_dictionary.keys())
print(len(list1))

"""
con = True
list1 = {"python", "c++", "javascript", "JAVA", "perl"}
list2 = {"perl", "bing", "google", "c++", "HTML", "PHP"}

ls = []
for i in list1:
    for j in list2:
        if i == j:
            con = False
    if con == True:
        ls.append(i)
    con = True

print(ls)
"""
