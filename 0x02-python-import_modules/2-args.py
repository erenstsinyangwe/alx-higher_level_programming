#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)
    if arg_count == 1:
        print("0 arguments.")
    lim = 2
    if arg_count == lim:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    if arg_count > lim:
        count = len(sys.argv) - 1
        print("{} arguments:".format(count))
        index = 1
        while index <= count:
            argument = sys.argv[index]
            print("{}: {}".format(index, argument))
            index += 1
