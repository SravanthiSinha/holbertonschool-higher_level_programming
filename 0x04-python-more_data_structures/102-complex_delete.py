#!/usr/bin/python3
def complex_delete(my_dict, value):
    if value not in my_dict.values() or my_dict == {}:
        return (my_dict)
    deletes = [x for x in my_dict if my_dict[x] == value]
    for x in deletes:
        del(my_dict[x])
    return (my_dict)
