class RangeIterator:
    """Iterator that yields numbers from start to end."""

    def __init__(self, start: int = 1, end: int = 10):
        """Initialize the iterator.

        Args:
            start: Starting number.
            end: Ending number.
        """
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next number.

        Raises:
            StopIteration: When the end is reached.
        """
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


if __name__ == "__main__":
    iterator = RangeIterator(1, 5)

    for num in iterator:
        print(num)

    print("\nManual next():")

    iterator = RangeIterator(1, 5)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    try:
        print(next(iterator))
    except StopIteration:
        print("StopIteration: Iterator is finished.")