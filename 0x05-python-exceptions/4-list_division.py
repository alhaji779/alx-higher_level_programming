#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    if (my_list_1 or my_list_2):

        for x in range(list_length):
            y = 0
            try:
                y = my_list_1[x] / my_list_2[x]
            except IndexError:
                print("out of range")
                pass
            except ZeroDivisionError:
                print("division by 0")
                pass
            except TypeError:
                print("wrong type")
                pass
            finally:
                new_list.append(y or 0)

        return (new_list)
