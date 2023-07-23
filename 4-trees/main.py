import random
from binary_search_tree import BinarySearchTree, UniqueNodeValuesViolation


if __name__ == "__main__":
    random.seed()

    bst = BinarySearchTree()
    for n in random.sample(range(1, 20), random.randint(5, 10)):
        try:
            bst.insert(n)
        except UniqueNodeValuesViolation:
            pass

    print("Binary Search Tree")
    print(str(bst))
    print(f"longest route: {bst.find_longest_route()}\n")

    new_element = random.randint(0, 9)
    while bst.contains(new_element):
        new_element = random.randint(0, 9)
    print(f"inserting new element: {new_element}:")
    bst.insert(new_element)
    print(str(bst))

