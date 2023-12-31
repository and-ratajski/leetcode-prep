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
        """Pop top element."""
        if self.height == 0:
            return None
        tmp = self.top
        self.top = self.top.next
        tmp.next = None
        self.height -= 1
        return tmp

    def peek(self) -> Any:
        """Peek (preview) top element."""
        if self.height == 0:
            return None
        return self.top.value


def is_balanced_parentheses(string: str) -> bool:
    """
    Checks if given string is parentheses-balanced or not.

    By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis
    in the correct order.
    """
    if len(string) in [0, 1]:
        return False

    parentheses_stack = Stack()
    for char in string:
        if char == "(":
            parentheses_stack.push(char)
        if char == ")":
            parentheses_stack.pop()
    return parentheses_stack.height == 0


def reverse_string(string: str) -> str:
    """Return a new string with the letters in reverse order, O(n)."""
    if len(string) in [0, 1]:
        return string

    stack = Stack()
    for char in string:
        stack.push(char)

    tmp_str = ""
    tmp_node = stack.top
    while tmp_node:
        tmp_str = tmp_str + tmp_node.value
        tmp_node = tmp_node.next
    return tmp_str


def sort_stack(stack: Stack) -> Stack:
    """Sorts stack elements in ascending order using only one additional stack, time O(n^2), space O(n)."""
    sorted_stack = Stack()
    tmp = None
    tmp_switch_count = -1

    while tmp_switch_count != 0:
        tmp_switch_count = 0
        for idx in range(stack.height, 0, -1):
            if idx == stack.height:
                tmp = stack.pop()

            if stack.peek() is None:
                sorted_stack.push(tmp.value)
            elif stack.peek() < tmp.value:
                sorted_stack.push(stack.pop().value)
                tmp_switch_count += 1
            else:
                sorted_stack.push(tmp.value)
                tmp = stack.pop()

        for idx in range(sorted_stack.height, 0, -1):
            stack.push(sorted_stack.pop().value)

    return stack
