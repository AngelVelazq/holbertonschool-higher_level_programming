#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_list = []
    for element in my_list:
        if element == search:
            replaced_list.append(replace)
        else:
            replaced_list.append(element)
    return replaced_list
