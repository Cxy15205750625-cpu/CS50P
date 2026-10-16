class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return “🍪” * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError

        self._size += n
        return self._size

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError
        self._size -= n
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

