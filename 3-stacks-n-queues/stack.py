from typing import Any


class Node:
    """Node (element) of a Linked List."""
    def __init__(self, value: Any):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)


class Stack:
    """Stack (FILO) implemented as a Linked List."""
    def __init__(self, value: Any = None):
        if value is None:
            self.top = None
            self.height = 0
        else:
            new_node = Node(value)
            self.top = new_node
            self.height = 1

    def __str__(self) -> str:
        tmp_str = ""
        offset = "   "
        tmp_node = self.top
        while tmp_node:
            tmp_node_str = str(tmp_node)
            tmp_str += "|" + \
                       offset[:len(offset)-len(tmp_node_str)] + \
                       tmp_node_str + \
                       offset[:len(offset)-len(tmp_node_str)-len(tmp_node_str) % 2] + \
                       "|\n"
            tmp_node = tmp_node.next
        return tmp_str + 2 * len(offset) * "-"

    def push(self, value: Any) -> None:
        """Push an element to the Stack."""
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        # return True

    def pop(self) -> Node | None:
        if self.height == 0:
            return None
        tmp = self.top
        self.top = self.top.next
        tmp.next = None
        self.height -= 1
        return tmp
