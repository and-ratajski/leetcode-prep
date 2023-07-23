import random
from queue import Queue, QueueOnStacks
from stack import Stack, is_balanced_parentheses, reverse_string, sort_stack

if __name__ == "__main__":
    random.seed()

    stack = Stack()
    [stack.push(n) for n in random.sample(range(1, 20), random.randint(5, 10))]

    print("stack:\n")
    print(str(stack) + "\n")

    new_element = random.randint(0, 9)
    print(f"pushing new element: {new_element}:\n")
    stack.push(new_element)
    print(str(stack) + "\n")

    print("popping (top) element:")
    print(str(stack.pop()) + "\n")
    print(str(stack) + "\n")

    print("sorted stack:\n")
    print(str(sort_stack(stack)) + "\n")

    string = "((()())(()))"
    print(f"check if the string: {string} is parentheses-balanced:\n")
    print(str(is_balanced_parentheses(string)) + "\n")

    string = "Some string to reverse using stack"
    print(f"reverse string: {string}:\n")
    print(str(reverse_string(string)) + "\n")

    queue = Queue()
    [queue.enqueue(n) for n in random.sample(range(1, 20), random.randint(5, 19))]

    print("queue:")
    print(str(queue) + "\n")

    new_element = random.randint(0, 9)
    print(f"enqueueing new element, O(1): {new_element}:")
    queue.enqueue(new_element)
    print(str(queue) + "\n")

    print("dequeueing (first) element, O(1):")
    print(queue.dequeue())
    print(str(queue) + "\n")

    queue_on_stacks = QueueOnStacks()
    [queue_on_stacks.enqueue(n) for n in random.sample(range(1, 20), random.randint(5, 19))]

    print("queue (using stacks):")
    print(str(queue_on_stacks) + "\n")

    new_element = random.randint(0, 9)
    print(f"enqueueing new element, O(n): {new_element}:")
    queue_on_stacks.enqueue(new_element)
    print(str(queue_on_stacks) + "\n")

    print("dequeueing (first) element, O(n):")
    print(queue_on_stacks.dequeue())
    print(str(queue) + "\n")
