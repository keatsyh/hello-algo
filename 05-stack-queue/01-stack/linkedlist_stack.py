from modules import ListNode


class LinkedListStack:
    def __init__(self):
        self._peek: ListNode | None = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, val: int):
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peek.val

    def to_list(self) -> list[int]:
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr


if __name__ == "__main__":
    stack = LinkedListStack()
    stack.push(1)
    stack.push(3)
    stack.push(2)
    stack.push(5)
    stack.push(4)
    print("栈 stack =", stack.to_list())

    # 访问栈顶元素
    peek: int = stack.peek()
    print("栈顶元素 peek =", peek)

    # 元素出栈
    pop: int = stack.pop()
    print("出栈元素 pop =", pop)
    print("出栈后 stack =", stack.to_list())

    # 获取栈的长度
    size: int = stack.size()
    print("栈的长度 size =", size)

    # 判断是否为空
    is_empty: bool = stack.is_empty()
    print("栈是否为空 =", is_empty)
