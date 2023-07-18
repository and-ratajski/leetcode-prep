import math


def task_3(h: int, w: int) -> (int, int):
    """
    Minimalize perimeter of a rectangular area of h and w. Returned values must
    be integers.
    """
    if w == 0 or h == 0:
        raise Exception("Fuck you!")
    area = h * w
    factors = set()
    float_solution = math.sqrt(h * w)

    divider = 2
    while len(factors) == 0:
        for value in range(int(math.sqrt(area)//divider), int(math.sqrt(area)*divider)):
            if area % value == 0:
                factors.add(value)
        divider *= 2

    smallest_diff = float(area)
    closest_factor = None
    for factor in factors:
        local_diff = abs(factor - float_solution)
        if local_diff < smallest_diff:
            smallest_diff = local_diff
            closest_factor = factor
    if not closest_factor:
        raise Exception("Couldn't find any :(")
    return closest_factor, int(area/closest_factor)


if __name__ == "__main__":
    print(task_3(216519845, 321698498))
    print(task_3(784289477, 1))  # prime number
