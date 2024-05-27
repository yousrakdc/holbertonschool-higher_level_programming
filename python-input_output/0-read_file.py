#!/usr/bin/python3

"""function that reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
    try:
        with open('my_file_0.txt', 'r', encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file 'my_file_0.txt' does not exist.")
    except IOError:
        print(f"Error: An error occurred while reading the file 'my_file_0.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
