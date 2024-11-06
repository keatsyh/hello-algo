class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None


def list_to_linked_list(arr: list[int]) -> ListNode | None:
    dum = head = ListNode(0)
    for a in arr:
        node = ListNode(a)
        head.next = node
        head = head.next
    return dum.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    arr: list[int] = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


if __name__ == "__main__":
    node1 = ListNode(0)
    node2 = ListNode(3)
    node3 = ListNode(5)
    node4 = ListNode(1)
    node5 = ListNode(9)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    arr2 = linked_list_to_list(node1)
    print(arr2)

    head2 = list_to_linked_list([9, 1, 4, 8, 6, 7])
    while head2:
        print(head2.val)
        head2 = head2.next
