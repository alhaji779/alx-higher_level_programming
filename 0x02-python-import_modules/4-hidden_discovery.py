#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    lst = dir(hidden_4)
    for x in lst:
        if (x[0] != "_"):
            print("{}".format(x))


