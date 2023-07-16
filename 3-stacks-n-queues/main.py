import random
from queue import Queue
from stack import Stack

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

    print("popping (last) element:")
    print(str(stack.pop()) + "\n")
    print(str(stack) + "\n")

    queue = Queue()
    [queue.enqueue(n) for n in random.sample(range(1, 20), random.randint(5, 19))]

    print("queue:")
    print(str(queue) + "\n")

    new_element = random.randint(0, 9)
    print(f"enqueueing new element: {new_element}:")
    queue.enqueue(new_element)
    print(str(queue) + "\n")

    print("dequeueing (first) element:")
    print(queue.dequeue())
    print(str(queue) + "\n")
