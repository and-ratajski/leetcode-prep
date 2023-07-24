from typing import Any


def have_common_item(list_1: list, list_2: list) -> bool:
    """Checks if two lists have at least one common item using dict (~ HashTable)."""
    el_dict = dict()
    for i in list_1:
        el_dict[i] = True

    for j in list_2:
        if j in el_dict:
            return True

    return False


class HashTable:
    """Basic implementation of a Hash Table in vanilla python."""

    default_initial_size = 7  # should be a prime nuber
    hashing_const = 23  # used by hashing function, should be a prime number

    def __init__(self, size=default_initial_size):
        self.data_map: list[list | None] = [None] * size

    def __str__(self):
        tmp = ""
        for idx, el in enumerate(self.data_map):
            tmp += str(idx) + ": " + str(el) + "\n"
        return tmp

    def _hash(self, key: str, hashing_param=hashing_const) -> int:
        """
        Custom (primitive) hash method to hash the keys.

        Mind that `hashing_const` should be a prime number.
        """
        _hash = 0
        for char in key:
            _hash = (_hash + ord(char) * hashing_param) % len(self.data_map)
        return _hash

    def set_item(self, key: str, value: Any()) -> None:
        """Sets item in the Hash Table."""
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key: str) -> Any | None:
        """Returns value(s) for a given key."""
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][1][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self) -> list[str]:
        """Returns all keys in the Hash Table."""
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
