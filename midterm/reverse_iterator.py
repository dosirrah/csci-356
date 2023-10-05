

class ReverseIterator:

    def __init__(self, x: list):
        self._x = x
        self._i = len(x)

    def __iter__(self):
        return self

    def __next__(self):
        self._i -= 1
        if self._i < 0:
            raise StopIteration
        return self._x[self._i]

            
