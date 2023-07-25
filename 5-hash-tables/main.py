import random
import string
from hash_table import (
    HashTable,
    have_common_item,
    find_duplicates,
    first_non_repeating_char,
    group_anagrams,
    two_sum
)


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


if __name__ == "__main__":
    random.seed()

    hash_table = HashTable()
    for _ in random.sample(range(1, 20), random.randint(5, 10)):
        key, value = randomword(random.randint(5, 20)), random.randint(10, 1000)
        hash_table.set_item(key, value)

    print("hash table:")
    print(hash_table)

    key, value = randomword(random.randint(5, 20)), random.randint(10, 1000)
    print(f"setting new key, value pair: {key, value}")
    hash_table.set_item(key, value)
    print(hash_table)

    keys = hash_table.keys()
    random_key = random.choice(keys)
    print(f"getting value for key: {random_key}")
    print(str(hash_table.get_item(random_key)) + "\n")

    list_1 = [n for n in random.sample(range(1, 20), random.randint(5, 10))]
    list_2 = [n for n in random.sample(range(1, 20), random.randint(5, 10))]
    print(f"check if lists: {list_1} and {list_2} have common element:")
    print(str(have_common_item(list_1, list_2)) + "\n")

    list_1 = [n for n in random.sample(range(5, 20), random.randint(5, 15))]
    list_1[-1] = list_1[0]
    print(f"find list: {list_1} duplicates:")
    print(str(find_duplicates(list_1)) + "\n")

    word = randomword(random.randint(5, 20))
    print(f"find first non-repeating char in string: {word}")
    print(str(first_non_repeating_char(word)) + "\n")

    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"group anagrams from given strings: {strings}")
    print(str(group_anagrams(strings)) + "\n")

    print("find the indices of two numbers in the array that add up to the target:")
    array = [n for n in random.sample(range(2, 12), random.randint(2, 10))]
    target = random.randint(5, 15)
    print(f"array: {array}, target: {target}")
    print(str(two_sum(array, target)) + "\n")
