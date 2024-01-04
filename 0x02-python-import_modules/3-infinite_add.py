#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    lst = []
    for i in args[1:]:
        lst.append(int(i))
    print(sum(lst))
