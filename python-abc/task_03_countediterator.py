#!/usr/bin/python3

"""CountedIterator - Keeping Track of Iteration"""


class CountedIterator:
    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        """convert the iterable into an iterator"""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself"""
        return self

    def __next__(self):
        """Return the next item from the iterator and increment the counter"""
        try:
            """Get the next item from the iterator"""
            item = next(self.iterator)
            """Increment the counter"""
            self.count += 1
            return item
        except StopIteration:
            """If the iterator is exhausted, raise StopIteration"""
            raise

    def get_count(self):
        """Return the count of the number of items iterated over."""
        return self.count


if __name__ == "__main__":
    """Create a list to be used with CountedIterator"""
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)
    print("Iterating through items:")

    try:
        """Iterate through the items in the CountedIterator"""
        while True:
            item = next(counted_iter)
            ount = counted_iter.get_count()
            print(f"Got {item}, total {count} items iterated.")
    except StopIteration:
        print("No more items.")
