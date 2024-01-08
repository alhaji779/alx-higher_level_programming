#!/usr/bin/python3

def element_at(my_list, idx):
     l = len(my_list)
     if idx < 0:
         return None
     elif idx > l:
         return None
     else:
         print("Element at index {:d} is {}".format(idx, myList[idx]))
