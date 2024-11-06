class ArrayQueue:
    def __init__(self, size: int):
        self._nums: list[int] = [0] * size
        self._front: int = 0
        self._size: int = 0

    def capacity(self) -> int:
        return len(self._nums)

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, num: int):
        if self.size() == self.capacity():
            raise IndexError("队列已满")
        rear: int = (self._front + self._size) % self.capacity()
        self._nums[rear] = num
        self._size += 1

    def pop(self) -> int:
        num = self.peek()
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("队列为空")
        return self._nums[self._front]

    def to_list(self) -> list[int]:
        res = [0] * self.size()
        j: int = self._front
        for i in range(self.size()):
            res[i] = self._nums[j % self.capacity()]
            j += 1
        return res


if __name__ == "__main__":
    # 初始化队列
    queue = ArrayQueue(10)

    # 元素入队
    queue.push(1)
    queue.push(3)
    queue.push(2)
    queue.push(5)
    queue.push(4)
    print("队列 queue =", queue.to_list())

    # 访问队首元素
    peek: int = queue.peek()
    print("队首元素 peek =", peek)

    # 元素出队
    pop: int = queue.pop()
    print("出队元素 pop =", pop)
    print("出队后 queue =", queue.to_list())

    # 获取队列的长度
    size: int = queue.size()
    print("队列长度 size =", size)

    # 判断队列是否为空
    is_empty: bool = queue.is_empty()
    print("队列是否为空 =", is_empty)

    # 测试环形数组
    for i in range(10):
        queue.push(i)
        queue.pop()
        print("第", i, "轮入队 + 出队后 queue = ", queue.to_list())
