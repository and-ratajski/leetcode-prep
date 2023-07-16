from typing import Any


class Node:
    """Node (element) of a Linked List."""
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)


class Queue:
    """Queue (FIFO) implemented as a Linked List."""
    def __init__(self, value: Any = None):
        if value is None:
            self.first = None
            self.last = None
            self.length = 0
        else:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1

    def __str__(self) -> str:
        tmp_str = "["
        tmp_node = self.first
        while tmp_node:
            tmp_str += str(tmp_node) + "|" if tmp_node.next else str(tmp_node)
            tmp_node = tmp_node.next
        return tmp_str + "]"

    def enqueue(self, value: Any) -> None:
        """Add an element to the queue."""
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        # return True

    def dequeue(self) -> Node | None:
        """Take an element from the queue."""
        if self.length == 0:
            return None
        tmp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            tmp.next = None
        self.length -= 1
        return tmp
