#!/usr/bin/python3

class Square():
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2 and 
                all(isinstance(num, int) for num in value) and 
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self._size ** 2

    def my_print(self):
        if self._size == 0:
            print()
            return
        [print() for _ in range(self._position[1])]
        for i in range(self._size):
            print(' ' * self._position[0] + '#' * self._size)

    def __str__(self):
        result = []
        if self._size == 0:
            return "\n"
        [result.append("") for _ in range(self._position[1])]
        for i in range(self._size):
            result.append(' ' * self._position[0] + '#' * self._size)
        return "\n".join(result)
