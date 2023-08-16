#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    for ele in range(len(my_list)):
        new_list[ele] = my_list[ele]
        for i in my_list:
            if 