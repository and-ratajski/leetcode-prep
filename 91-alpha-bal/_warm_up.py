import random


def fizzBuzz(n: int) -> None:
    """Warmup task."""
    if n < 0 or n > 2 * 10**5:
        raise Exception("n is not within function domain")

    for n in range(n):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0 and n % 5 != 0:
            print("Fizz")
        elif n % 3 != 0 and n % 5 == 0:
            print("Buzz")
        else:
            print(n)


if __name__ == "__main__":
    for n in random.sample(range(1, 20), random.randint(5, 10)):
        fizzBuzz(n)
