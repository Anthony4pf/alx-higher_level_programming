#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print("{}".format(argc - 1))
    else:
        sum_arg = 0
        for i in range(1, argc):
            sum_arg += int(argv[i])
        print("{}".format(sum_arg))
