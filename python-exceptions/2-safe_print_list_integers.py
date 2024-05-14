#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed_elements = []

    try:
        for i in range(x):
            element = my_list[i]
            if isinstance(element, int):
                printed_elements.append(str(element))
                count += 1
    except IndexError:
        pass

    print("{:d}".format(", ".join(printed_elements)))
    return count
