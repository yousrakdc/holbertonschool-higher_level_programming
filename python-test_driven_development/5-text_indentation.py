#!/usr/bin/python3

"""function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = {'.', '?', ':'}

    result = ""
    for char in text:
        result += char
        if char in special_chars:
            result += "\n\n"

    lines = [line.strip() for line in result.split("\n")]
    formatted_text = "\n".join(lines)

    print(formatted_text)
