import math


def task_3(h: int, w: int) -> (int, int):
    """
    Minimalize perimeter of a rectangular area of h and w. Returned values must
    be integers.
    """
    area = h * w
    factors = set()
    float_solution = math.sqrt(h * w)

    for value in range(int(math.sqrt(area)//2), int(math.sqrt(area)*2)):
        if area % value == 0:
            factors.add(value)

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
