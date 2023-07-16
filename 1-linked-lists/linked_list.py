from typing import Any
from typing_extensions import Self


class Node:
    """Node (element) of a Linked List."""
    def __init__(self, value: Any):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)


class CustomSet:
    """Custom (quick) implementation of set in order to speed up some algorithms."""
    def __init__(self, *args):
        self._dict = dict()
        for arg in args:
            self.add(arg)

    def add(self, item: Any) -> None:
        """Add item to the set."""
        self._dict[item] = item

    def remove(self, item: Any) -> None:
        """Remove item from the set."""
        del self._dict[item]

    def contains(self, item) -> bool:
        """ Check whether the set contains a certain item. """
        return item in self._dict


class LinkedList:
    """Linked List implemented as a vanilla python class."""
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

    def append(self, value: Any) -> Self:
        """Append an element to the list - returns self instance."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def pop(self) -> Node | None:
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

    def prepend(self, value: Any) -> Self:
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
        """Reverse the list (with gap)."""
        tmp = self.head
        self.head = self.tail
        self.tail = tmp
        before = None
        for _ in range(self.length):
            after = tmp.next
            tmp.next = before
            before = tmp
            tmp = after

    def reverse_recur(self, _node_ref: Node | None = None) -> Self:
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
            tmp = current.next
            # Detach temp and connect current to next node
            current.next = tmp.next
            # Place temp at the beginning of the reversed section
            tmp.next = prev.next
            # Connect temp to the part before the reversed section
            prev.next = tmp

        # Update the head of the list if necessary
        self.head = dummy.next

    def partition_list(self, x: int) -> None:
        """
        Partition the linked list such that all nodes with values less than x come before nodes with values greater
        than or equal to x. Preserve the original relative order of the nodes in each of the two partitions.

        You should create two new linked lists. These two linked lists will be made up of the original nodes from the
        linked list that is being partitioned, one for nodes less than x and one for nodes greater than or equal to x.
        None of the nodes from the linked list should be duplicated.
        """
        if self.length == 0:
            return None
        ld_list = LinkedList()
        ge_list = LinkedList()

        tmp = self.head
        while tmp:
            if tmp.value < x:
                ld_list.append(tmp.value)
            else:
                ge_list.append(tmp.value)
            tmp = tmp.next

        # merge two lists
        ld_list.tail.next = ge_list.head
        # ld_list.tail = ge_list.tail
        self.head = ld_list.head
        self.tail = ge_list.tail

    def remove_duplicates(self) -> None:
        """
        Removes all duplicate values from the list.

        Method should not create a new list, but rather modify the existing list in-place, preserving the relative
        order of the nodes.

        You can implement the remove_duplicates() method in two different ways:

        * Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked
        list. You are allowed to use the provided Set data structure in your implementation.

        * Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in
        the linked list. You are not allowed to use any additional data structures for this implementation.
        """
        tmp_set = CustomSet()
        prev = Node(0)
        prev.next = self.head
        tmp = self.head

        while tmp:
            if tmp_set.contains(tmp.value):  # O(1)
                if tmp.next:
                    prev.next = tmp.next
                else:
                    prev.next = None
                    self.tail = prev
                self.length -= 1
            else:
                prev = tmp
            tmp_set.add(tmp.value)  # O(1)
            tmp = tmp.next
