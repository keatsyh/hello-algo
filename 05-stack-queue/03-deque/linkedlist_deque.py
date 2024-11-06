class ListNode:
    def __init__(self, val):
        self.val: int = val
        self.next: ListNode | None = None
        self.prev: ListNode | None = None


class LinkedListDeque:
    def __init__(self):
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self.size() == 0

    def push(self, num: int, is_front: bool):
        node = ListNode(num)
        if self.is_empty():
            self._front = self._rear = node
        elif is_front:
            self._front.prev = node
            node.next = self._front
            self._front = node
        else:
            self._rear.next = node
            node.prev = self._rear
            self._rear = node
        self._size += 1

    def push_first(self, num: int):
        self.push(num, True)

    def push_last(self, num: int):
        self.push(num, False)

    def pop(self, is_front: bool) -> int:
        if is_front:
            val: int = self.peek_first()
            fnext: ListNode | None = self._front.next
            if fnext is not None:
                fnext.prev = None
                self._front.next = None
            self._front = fnext
        else:
            val: int = self.peek_last()
            rprev: ListNode | None = self._rear.prev
            if rprev is not None:
                rprev.next = None
                self._rear.prev = None
            self._rear = rprev
        self._size -= 1
        return val

    def pop_first(self) -> int:
        return self.pop(True)

    def pop_last(self) -> int:
        return self.pop(False)

    def peek_first(self) -> int:
        if self.is_empty():
            raise IndexError("双向队列为空")
        return self._front.val

    def peek_last(self) -> int:
        if self.is_empty():
            raise IndexError("双向队列为空")
        return self._rear.val

    def to_list(self) -> list[int]:
        node = self._front
        res = []
        while node:
            val = node.val
            res.append(val)
            node = node.next
        return res


if __name__ == "__main__":
    # 初始化双向队列
    deque = LinkedListDeque()
    deque.push_last(3)
    deque.push_last(2)
    deque.push_last(5)
    print("双向队列 deque =", deque.to_list())

    # 访问元素
    peek_first: int = deque.peek_first()
    print("队首元素 peek_first =", peek_first)
    peek_last: int = deque.peek_last()
    print("队尾元素 peek_last =", peek_last)

    # 元素入队
    deque.push_last(4)
    print("元素 4 队尾入队后 deque =", deque.to_list())
    deque.push_first(1)
    print("元素 1 队首入队后 deque =", deque.to_list())

    # 元素出队
    pop_last: int = deque.pop_last()
    print("队尾出队元素 =", pop_last, "，队尾出队后 deque =", deque.to_list())
    pop_first: int = deque.pop_first()
    print("队首出队元素 =", pop_first, "，队首出队后 deque =", deque.to_list())

    # 获取双向队列的长度
    size: int = deque.size()
    print("双向队列长度 size =", size)

    # 判断双向队列是否为空
    is_empty: bool = deque.is_empty()
    print("双向队列是否为空 =", is_empty)
