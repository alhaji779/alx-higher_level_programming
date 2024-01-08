def replace_in_list(my_list, idx, element):
    ll = my_list.copy()
    if(idx < 0 or idx >= len(my_list)):
        return(my_list)
    ll[idx] = element
    return(ll)
