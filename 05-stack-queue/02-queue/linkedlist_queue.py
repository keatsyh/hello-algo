from modules import ListNode


class LinkedListQueue:
    def __init__(self):
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, num: int):
        node = ListNode(num)
        if self.is_empty():
            self._front = self._rear = node
        else:
            self._rear.next = node # 链
            self._rear = node # 指
        self._size += 1

    def pop(self) -> int:
        num = self.peek()
        self._front = self._front.next
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val

    def to_list(self):
        queue: list[int] = []
        front = self._front
        while front:
            queue.append(front.val)
            front = front.next
        return queue


if __name__ == "__main__":
    # 初始化队列
    queue = LinkedListQueue()

    # 元素入队
    queue.push(1)
    queue.push(3)
    queue.push(2)
    queue.push(5)
    queue.push(4)
    print("队列 queue =", queue.to_list())

    # 访问队首元素
    peek: int = queue.peek()
    print("队首元素 front =", peek)

    # 元素出队
    pop_front: int = queue.pop()
    print("出队元素 pop =", pop_front)
    print("出队后 queue =", queue.to_list())

    # 获取队列的长度
    size: int = queue.size()
    print("队列长度 size =", size)

    # 判断队列是否为空
    is_empty: bool = queue.is_empty()
    print("队列是否为空 =", is_empty)