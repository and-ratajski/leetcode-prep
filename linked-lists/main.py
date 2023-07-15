import random
from linked_list import LinkedList

if __name__ == "__main__":
    random.seed()

    linked_list = LinkedList()
    [linked_list.append(n) for n in random.sample(range(1, 20), random.randint(5, 19))]

    print("linked list:")
    print(str(linked_list) + "\n")

    new_element = random.randint(0, 9)
    print(f"appending new element: {new_element}:")
    linked_list.append(new_element)
    print(str(linked_list) + "\n")

    print("popping last element:")
    print(linked_list.pop())
    print(str(linked_list) + "\n")

    new_element = random.randint(0, 9)
    print(f"prepending new element: {new_element}:")
    linked_list.prepend(new_element)
    print(str(linked_list) + "\n")

    print("popping first element:")
    print(linked_list.pop_first())
    print(str(linked_list) + "\n")

    random_index, random_value = random.randint(0, linked_list.length-1), random.randint(0, 20)
    print(f"setting value of: {random_value} to the element of index: {random_index}:")
    linked_list.set_value(random_index, random_value)
    print(str(linked_list) + "\n")

    random_index, random_value = random.randint(0, linked_list.length-1), random.randint(0, 20)
    print(f"inserting new element: {random_value} at index: {random_index}:")
    linked_list.insert(random_index, random_value)
    print(str(linked_list) + "\n")

    random_index = random.randint(0, linked_list.length-1)
    print(f"removing an element at index: {random_index}:")
    linked_list.remove(random_index)
    print(str(linked_list) + "\n")

    linked_list.reverse()
    print("reversed list:")
    print(str(linked_list) + "\n")

    linked_list = linked_list.reverse_recur()
    print("reversed list (recursion):")
    print(str(linked_list) + "\n")

    print("middle node in the list:")
    assert linked_list.find_middle_node() == linked_list.get(linked_list.length//2)
    print(str(linked_list.find_middle_node()) + "\n")

    print("does the list have a loop:")
    print(str(linked_list.has_loop()) + "\n")

    k = random.randint(1, linked_list.length)
    print(f"{k}. element from the end:")
    print(str(linked_list.find_kth_from_end(k)) + "\n")

    j = random.randint(0, linked_list.length//2-1)
    k = random.randint(linked_list.length//2, linked_list.length-1)
    print(f"reversed list from {j}. to {k}. element:")
    linked_list.reverse_between(j, k)
    print(str(linked_list) + "\n")
