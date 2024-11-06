class ArrayDeque:

    def __init__(self, capacity: int):
        self._nums: list[int] = [0] * capacity
        self._front: int = 0
        self._size: int = 0


    def size(self):
        return self._size