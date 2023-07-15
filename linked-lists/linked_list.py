from typing import Any


class Node:
    """Node (element) of a linked list"""
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    """Linked list implemented as a vanilla python class"""
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

    def __str__(self):
        tmp_str = "["
        tmp_node = self.head
        while tmp_node:
            tmp_str += str(tmp_node) + ", " if tmp_node.next else str(tmp_node)
            tmp_node = tmp_node.next
        return tmp_str + "]"

    def print_list(self):
        temp = self.head
        acc = 0
        while temp and acc < 20:
            print(temp.value)
            temp = temp.next
            acc += 1

    def append(self, value: Any):
        """Append an element to the list - returns self instance"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        """Pop last element from the list."""
        if self.length == 0:
            return None
        tmp = self.head
        pre = self.head
        while tmp.next:
            pre = tmp
            tmp = tmp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return tmp

    def prepend(self, value: Any):
        """Prepend an element to the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def pop_first(self) -> Node | None:
        """Pop first element from the list."""
        if self.length == 0:
            return None
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return tmp

    def get(self, index: int) -> Node | None:
        """Get element at 'index' position."""
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        return tmp

    def set_value(self, index: int, value: Any) -> bool:
        """Set an element at 'index' position."""
        tmp = self.get(index)
        if tmp:
            tmp.value = value
            return True
        return False

    def insert(self, index: int, value: Any):
        """Insert a node of given value at 'index' position."""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        tmp = self.get(index - 1)
        new_node.next = tmp.next
        tmp.next = new_node
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
        pre = self.get(index - 1)
        tmp = pre.next
        pre.next = tmp.next
        tmp.next = None
        self.length -= 1
        return tmp

    def reverse(self) -> None:
        """Reverse the list."""
        tmp = self.head
        self.head = self.tail
        self.tail = tmp
        before = None
        for _ in range(self.length):
            after = tmp.next
            tmp.next = before
            before = tmp
            tmp = after

    def reverse_recur(self, _node_ref: Node | None = None):
        """Reverse the list in recurring fashion - returns reverted copy."""
        if not _node_ref:
            _node_ref = self.head

        match _node_ref.next:
            case None:
                return LinkedList(_node_ref.value)
            case _:
                return self.reverse_recur(_node_ref.next).append(_node_ref.value)

    def find_middle_node(self) -> Node:
        """Get middle node or the fist one of the second half (for even list length)."""
        if self.head.next is None:
            return self.head
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

    def has_loop(self) -> bool | Node:
        """Basically, check if all pointers (next) point to the right node - no looping."""
        if self.head.next is None:
            return self.head
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if id(slow_ptr) == id(fast_ptr):
                return True
        return False

    def find_kth_from_end(self, k: int) -> Node | None:
        """Analogy to python's list[-k]."""
        if k <= 0:
            return None
        if k == 1:
            return self.tail
        slow_ptr = self.head
        fast_ptr = self.head
        fast_pos = 0

        while fast_ptr is not None:
            fast_pos += 1
            if fast_pos <= k:
                fast_ptr = fast_ptr.next
                continue
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next

        return None if fast_pos < k else slow_ptr

    def reverse_between(self, j: int, k: int) -> None:
        """
        Reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place without
        using tail.

        Constrains: time complexity of O(n) and space complexity of O(1).
        """
        if self.length <= 1:
            return

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(j):
            prev = prev.next
        current = prev.next

        for _ in range(k - j):
            # Set temp to the next node to be reversed
            temp = current.next
            # Detach temp and connect current to next node
            current.next = temp.next
            # Place temp at the beginning of the reversed section
            temp.next = prev.next
            # Connect temp to the part before the reversed section
            prev.next = temp

        # Update the head of the list if necessary
        self.head = dummy.next
