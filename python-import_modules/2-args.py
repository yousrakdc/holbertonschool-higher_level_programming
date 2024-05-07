#!/usr/bin/python3
import sys


def main():
    argv = sys.argv

    num_args = len(argv) - 1

    if num_args == 1:
        print("1 argument:")
    elif num_args == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(num_args))

    if num_args > 0:

        for i in range(1, len(argv)):

            print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
