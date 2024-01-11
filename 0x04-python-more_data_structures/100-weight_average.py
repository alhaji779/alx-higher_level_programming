#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    if (my_list):
        my_l = dict(my_list)
        return (sum([k*v for k, v in my_l.items()]) / sum(my_l.values()))
    else:
        return (0)
