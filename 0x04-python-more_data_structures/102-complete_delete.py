def complex_delete(a_dictionary, value):
    if (value):
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
        return (a_dictionary)
