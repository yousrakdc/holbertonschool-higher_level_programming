#!/usr/bin/python3
print(
    "".join(
        f"{chr(i)}"
        for i in range(97, 123)
        if chr(i) not in ('q', 'e')
    ),
    end=''
)
