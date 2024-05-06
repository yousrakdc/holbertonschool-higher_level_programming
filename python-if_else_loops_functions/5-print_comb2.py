#!/usr/bin/python3
formatted_numbers = ", ".join("{:02}".format(i) for i in range(100))
print(formatted_numbers)
