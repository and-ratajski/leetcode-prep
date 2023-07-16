import random
from doubly_linked_list import DoublyLinkedList

if __name__ == "__main__":
    random.seed()

    doubly_linked_list = DoublyLinkedList()
    [doubly_linked_list.append(n) for n in random.sample(range(1, 20), random.randint(5, 19))]

    print("doubly linked list:")
    print(str(doubly_linked_list) + "\n")

    new_element = random.randint(0, 9)
    print(f"appending new element: {new_element}:")
    doubly_linked_list.append(new_element)
    print(str(doubly_linked_list) + "\n")

    print("popping last element:")
    print(doubly_linked_list.pop())
    print(str(doubly_linked_list) + "\n")

    new_element = random.randint(0, 9)
    print(f"prepending new element: {new_element}:")
    doubly_linked_list.prepend(new_element)
    print(str(doubly_linked_list) + "\n")

    print("popping first element:")
    print(doubly_linked_list.pop_first())
    print(str(doubly_linked_list) + "\n")

    random_index, random_value = random.randint(0, doubly_linked_list.length-1), random.randint(0, 20)
    print(f"setting value of: {random_value} to the element of index: {random_index}:")
    doubly_linked_list.set_value(random_index, random_value)
    print(str(doubly_linked_list) + "\n")

    random_index, random_value = random.randint(0, doubly_linked_list.length-1), random.randint(0, 20)
    print(f"inserting new element: {random_value} at index: {random_index}:")
    doubly_linked_list.insert(random_index, random_value)
    print(str(doubly_linked_list) + "\n")

    random_index = random.randint(0, doubly_linked_list.length-1)
    print(f"removing an element at index: {random_index}:")
    doubly_linked_list.remove(random_index)
    print(str(doubly_linked_list) + "\n")

    print("swapping first and last elements:")
    doubly_linked_list.swap_first_last()
    print(str(doubly_linked_list) + "\n")

    print("reversed list:")
    doubly_linked_list.reverse()
    print(str(doubly_linked_list))
    print("check (print from the end):")
    print(doubly_linked_list.str_from_end() + "\n")

    print("Check if the list is a palindrome:")
    print(str(doubly_linked_list.is_palindrome()) + "\n")

    print("Swap pairs in list")
    doubly_linked_list.swap_pairs()
    print(str(doubly_linked_list))
    print("check (print from the end):")
    print(doubly_linked_list.str_from_end() + "\n")
