#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
    return(sum(new_list))
