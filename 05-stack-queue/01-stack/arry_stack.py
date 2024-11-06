class ArrayStack:
    def __init__(self):
        self._stack: list[int] = []

    def size(self):
        return len(self._stack)

    def is_empty(self):
        return self.size() == 0

    def push(self, val: int):
        self._stack.append(val)

    def pop(self) -> int:
        return self._stack.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack[-1]

    def to_list(self) -> list[int]:
        return self._stack


if __name__ == "__main__":
    stack = ArrayStack()
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
