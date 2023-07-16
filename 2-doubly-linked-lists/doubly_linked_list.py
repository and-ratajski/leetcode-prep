from typing import Any


class Node:
    """Node (element) of a Doubly Linked List."""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.value)


class DoublyLinkedList:
    """Doubly Linked List implemented as a vanilla python class."""
    def __init__(self, value: Any = None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def __str__(self) -> str:
        tmp_str = "["
        tmp_node = self.head
        while tmp_node:
            tmp_str += str(tmp_node) + ", " if tmp_node.next else str(tmp_node)
            tmp_node = tmp_node.next
        return tmp_str + "]"

    def str_from_end(self) -> str:
        """Print list from the end."""
        tmp_str = "["
        tmp_node = self.tail
        while tmp_node:
            tmp_str += str(tmp_node) + ", " if tmp_node.prev else str(tmp_node)
            tmp_node = tmp_node.prev
        return tmp_str + "]"

    def append(self, value) -> bool:
        """Append an element to the list - returns self instance"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Node | None:
        """Pop last element from the list."""
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value: Any) -> bool:
        """Prepend an element to the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node | None:
        """Pop first element from the list."""
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index: int) -> Node | None:
        """Get element at 'index' position."""
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index: int, value: Any) -> bool:
        """Set an element at 'index' position."""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index: int, value: Any) -> bool:
        """Insert a node of given value at 'index' position."""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index: int) -> Node | None:
        """Remove a node of given index from the list."""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

    def swap_first_last(self) -> None:
        """Swaps the values of the first and last node"""
        tmp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = tmp

    def reverse(self) -> None:
        """Reverse the list (with dummy Node)."""
        self.tail = self.head
        tmp = self.head
        before = Node(0)
        before.next = self.head

        while tmp and tmp.next:
            after = tmp.next
            if after.next:
                after.next.prev = tmp

            tmp.next = after.next
            before.next.prev = after

            after.next = before.next
            after.prev = None

            before.next = after

        self.head = before.next

    def is_palindrome(self) -> bool:
        """Checks whether a given doubly linked list reads the same forwards and backwards."""
        return self.__str__() == self.str_from_end()

    def swap_pairs(self) -> None:
        """Swaps the values of adjacent nodes in the linked list."""
        match self.length:
            case 0:
                return None
            case 1:
                return None

        last_el = None
        if self.length % 2 == 1:
            last_el = self.pop()

        before = Node(0)
        before.next = self.head
        tmp = self.head

        self.head = self.head.next
        self.tail = self.tail.prev
        while tmp and tmp.next:
            after = tmp.next

            tmp.next = after.next
            tmp.prev = after

            after.next = tmp
            # after.next.prev = tmp
            after.prev = before

            before.next = after

            before = tmp
            tmp = tmp.next

        if last_el:
            self.append(last_el)
        self.head.prev = None
