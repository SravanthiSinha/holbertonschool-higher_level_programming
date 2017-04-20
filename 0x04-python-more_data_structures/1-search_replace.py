#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return ([x if x is not search else replace for x in my_list])
