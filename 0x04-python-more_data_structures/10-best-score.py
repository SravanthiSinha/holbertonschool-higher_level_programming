#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None or my_dict == {}:
        return (None)
    if isinstance(my_dict, dict) is False:
        return (None)
    if max(my_dict, key=my_dict.get) is 0:
        return (None)
    return(max(my_dict, key=my_dict.get))
