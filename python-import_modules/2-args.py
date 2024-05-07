#!/usr/bin/python3
import sys


def main():
    argv = sys.argv

    num_args = len(argv) - 1
    separator = ':' if num_args > 0 else '.'

    arg_word = "argument" if num_args == 1 else "arguments"

    output = "Number of {}{}{}".format(arg_word, separator, num_args)

    print(output)

    if num_args > 0:
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
