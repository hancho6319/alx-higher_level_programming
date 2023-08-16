#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_list_new = my_list.copy()
    for i in range(len(my_list)):
        if my_list_new[i] == search:
            my_list_new[i] = replace
    return my_list_new
