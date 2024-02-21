#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    num = 0

    for item in my_list:
        if item not in my_set:
            my_set.add(item)
            num += item

    return (num)
