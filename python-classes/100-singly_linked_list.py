#!/usr/bin/python3

"""Singly linked list, just why"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a Node instance."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data value of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data value of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the linked list."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes an empty SinglyLinkedList instance."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = ""
        current_node = self.__head
        while current_node:
            result += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return result.strip()

    def sorted_insert(self, value):
        new_node = Node(value)

        if not self.__head or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current_node = self.__head
        while current_node.next_node and value > current_node.next_node.data:
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
