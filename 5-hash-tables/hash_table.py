from typing import Any


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

    def set_item(self, key: str, value: Any) -> None:
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
                if self.data_map[index][i][0] == key:
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


def have_common_item(list_1: list, list_2: list) -> bool:
    """Checks if two lists have at least one common item using dict (~ HashTable)."""
    el_dict = dict()
    for i in list_1:
        el_dict[i] = True

    for j in list_2:
        if j in el_dict:
            return True

    return False


def find_duplicates(a_list: list) -> list:
    """Returns duplicates from a given list using a dict (~ HashTable)."""
    el_dict = dict()
    already_added = dict()
    duplicates = []

    for i in a_list:
        if i in el_dict:
            if i not in already_added:
                duplicates.append(i)
                already_added[i] = True
        else:
            el_dict[i] = True
    return duplicates


def first_non_repeating_char(string: str) -> str | None:
    """Returns first non-repeating char in the string."""
    string_as_list = [*string]
    duplicates = find_duplicates(string_as_list)
    for char in string_as_list:
        if char not in duplicates:
            return char
    return None


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Groups strings into anagrams (containing the same letters)."""
    hash_table = HashTable()

    for string in strings:
        hash_table.set_item(string, string)
    non_nones = [el for el in hash_table.data_map if el is not None]
    return [[anagram[0] for anagram in el] for el in non_nones]


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and a target integer target,
    find the indices of two numbers in the array that add up to the target.
    """
    hash_table_normal = HashTable(target)
    hash_table_reverted = HashTable(target)

    def _custom_hash_normal(key: int):
        """Custom hash function implementation for the purpose of this task."""
        return key % target

    def _custom_hash_reverted(key: int):
        """Custom hash function implementation for the purpose of this task."""
        return (target - key) % target

    hash_table_normal._hash = _custom_hash_normal
    hash_table_reverted._hash = _custom_hash_reverted

    for idx, num in enumerate(nums):
        if num <= target:
            hash_table_normal.set_item(num, idx)  # noqa
            hash_table_reverted.set_item(num, idx)  # noqa

    for key in hash_table_normal.keys():
        match = hash_table_reverted.get_item(target - key)  # noqa
        if match is not None:
            if key == target - key:  # noqa
                # Must differentiate between [3, 3], 6 and [1, 1, 3], 6
                is_duplicate = len(hash_table_normal.data_map[key]) > 1  # noqa
                if is_duplicate:
                    return [
                        indices[1] for indices in hash_table_normal.data_map[key]  # noqa
                    ]
                else:
                    continue
            return [match, hash_table_normal.get_item(key)]
    return []


def two_sum_solution(nums: list[int], target: int) -> list[int]:
    """Cleaner solution for `two_sum` function."""
    num_map = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], idx]
        num_map[num] = idx
    return []


def subarray_sum(nums: list[int], target: int) -> list[int]:
    """
    Finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).
    """
    subsums = dict()

    for idx, num in enumerate(nums):
        subsums[idx] = []
        sub_idx = idx
        while sub_idx >= 0:
            try:
                last_value = subsums[sub_idx][-1]
            except IndexError:
                last_value = 0
            if num == target:
                return [sub_idx, sub_idx]
            elif last_value + num == target:
                return [sub_idx, len(subsums[sub_idx]) + sub_idx]
            subsums[sub_idx].append(last_value + num)
            sub_idx -= 1
    return []


def subarray_sum_solution(nums: list[int], target: int) -> list[int]:
    """Cleaner solution for `subarray_sum` function."""
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []
