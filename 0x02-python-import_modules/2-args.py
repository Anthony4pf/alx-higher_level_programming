#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv)

    if len_argv == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len_argv - 1))
        i = 1
        while i < len_argv:
            print("{}: {}".format(i, sys.argv[1]))
            i += 1
