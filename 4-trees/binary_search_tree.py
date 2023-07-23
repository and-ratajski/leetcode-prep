class UniqueNodeValuesViolation(Exception):
    """Thrown when there is already such value present in the Three."""

    pass


class TreeNode:
    """Node of a Binary Search Tree"""

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    """Binary Search Tree implementation in python."""

    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root is None:
            return "Tree is empty."

        _tree_depth, _ = self.find_longest_route()
        _tree_dict = self._tree_2_dict(self.root, 0, _tree_depth)
        tmp_str = ""
        for level in range(0, _tree_depth):
            tmp_str += _tree_dict[str(level)] + "\n"
        return tmp_str

    def _tree_2_dict(
        self,
        node: TreeNode,
        level: int,
        tree_depth: int | None = None,
        tree_dict: dict | None = None,
        offset: int = 0,
    ) -> dict:
        if tree_dict is None:
            tree_dict = {}
        if tree_depth is None:
            tree_depth, _ = self.find_longest_route()

        if tree_dict.get(str(level), False):
            tree_dict[str(level)] = (
                tree_dict[str(level)] + " " + str(node) + " " * (len(str(node)) % 2)
            )
        else:
            tree_dict[str(level)] = (
                " " * ((tree_depth - level) + ((offset + 1) * level))
                + " " * (tree_depth - level)
                + " " * (len(str(node)) % 2)
                + str(node)
                + " "
            )

        if node.left:
            tree_dict = {
                **tree_dict,
                **self._tree_2_dict(
                    node.left, level + 1, tree_depth, tree_dict, offset
                ),
            }
        elif tree_dict.get(str(level + 1), False):
            tree_dict[str(level + 1)] = tree_dict.get(str(level + 1), "") + " "
        if node.right:
            tree_dict = {
                **tree_dict,
                **self._tree_2_dict(
                    node.right, level + 1, tree_depth, tree_dict, offset + 1
                ),
            }
        elif tree_dict.get(str(level + 1), False):
            tree_dict[str(level + 1)] = tree_dict.get(str(level + 1), "") + " "
        return tree_dict

    def find_longest_route(self) -> (int, list[TreeNode]):
        if self.root is None:
            return 0, []

        longest_path_count, longest_path = self._longest_path(self.root)
        return longest_path_count, longest_path

    def _longest_path(self, node: TreeNode) -> (int, list[TreeNode]):
        if node is None:
            return 0, []

        left_depth, left_path = self._longest_path(node.left)
        right_depth, right_path = self._longest_path(node.right)

        if left_depth > right_depth:
            return left_depth + 1, left_path + [node.value]
        else:
            return right_depth + 1, right_path + [node.value]

    def insert(self, value: int) -> None:
        """Insert a new Node of value 'value' to the Three"""
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        tmp = self.root
        while True:
            if new_node.value < tmp.value:
                if tmp.left is None:
                    tmp.left = new_node
                    return
                tmp = tmp.left
            elif new_node.value > tmp.value:
                if tmp.right is None:
                    tmp.right = new_node
                    return
                tmp = tmp.right
            else:
                raise UniqueNodeValuesViolation(
                    "Nodes in a BinarySearchThree have to have unique values."
                )

    def contains(self, value: int) -> bool:
        """Checks if the Tree contains given value."""
        tmp = self.root
        while tmp is not None:
            if value < tmp.value:
                tmp = tmp.left
            elif value > tmp.value:
                tmp = tmp.right
            else:
                return True
        return False
