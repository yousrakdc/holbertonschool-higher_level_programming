#!/usr/bin/python3


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data value of the node."""
        return self.__data

    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        new_node = Node(value)
