#!/usr/bin/python3

"""Extending the Python List with Notifications"""


class VerboseList(list):
    def append(self, item):
        """Override append to add a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Override extend to add a notification."""
        num_items = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{num_items}] items.")

    def remove(self, item):
        """Override remove to add a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        """Override pop to add a notification."""
        if index is None:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
            return item
        else:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
