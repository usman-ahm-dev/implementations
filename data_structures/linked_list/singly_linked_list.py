class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        iter = self.head
        while iter:
            print(iter.value, "->", end="")
            iter = iter.next

    def size(self) -> int:
        iter = self.head
        size = 0
        while iter:
            size += 1
        return size

    def value_at(self, index):
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        iter = self.head
        for i in range(index + 1):
            iter = iter.next
        return iter.value

    def push_front(self, value):
        self.head = Node(value, self.head)

    def pop_front(self):
        value = self.head.value
        self.head = self.head.next
        return value

    def push_back(self, value):
        iter = self.head
        while iter:
            iter = iter.next
        iter.next = Node(value)

    def pop_back(self):
        iter = self.head
        while iter:
            iter = iter.next
        value = iter.value
        iter = None
        return value

    def insert(self, index, value):
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        iter = self.head
        for i in range(index + 1):
            iter = iter.next
        iter = Node(value, iter)

    def erase(self, index):
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        iter = self.head
        for i in range(index):
            iter = iter.next
        iter.next = iter.next.next

    def value_n_from_end(self, index):
        pass

    def reverse(self):
        current = self.head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

    def remove_value(self, value):
        iter = self.head
        while iter:
            if iter.next.value == value:
                iter.next = iter.next.next
