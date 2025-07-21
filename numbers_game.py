from itertools import permutations
from operator import mul, truediv, add, sub
import sys


# TODO 4-4s / nubble with stack based theory
# TODO format to release in order of length


def mydiv(a, b):
    result = truediv(a, b)
    if int(result) == result:
        return int(result)
    else:
        raise ValueError


operations = [(add, "+"), (sub, "-"), (mul, "*"), (mydiv, "/")]


def represent_stack(stack):
    reps = [str(item) if type(item) is int else item[1] for item in stack]
    return " ".join(reps)


def evaluate(stack) -> int:
    try:
        total = 0
        last_operation = add
        for item in stack:
            if type(item) is int:
                total = last_operation(total, item)
            else:
                last_operation = item[0]

        return total
    except ValueError:
        return 0


def solve(target, numbers):
    for r in range(1, len(numbers) + 1):
        orderings = permutations(numbers, r)
        if r == 1:
            for ordering in orderings:
                if ordering[0] != target:
                    continue
                print(ordering[0])
            continue
        ops = list(permutations(operations, r - 1))
        for ordering in orderings:
            for op_series in ops:
                stack = []
                for i, n in enumerate(ordering):
                    stack.append(n)
                    if i != len(ordering) - 1:
                        stack.append(op_series[i])
                stack_result = evaluate(stack)
                if stack_result == target:
                    print(f"{represent_stack(stack)} = {target}")


def play():
    try:
        numbers = [int(x) for x in input("Numbers: ").split()]
    except ValueError:
        sys.exit()

    target = int(input("Target: "))

    solve(target, numbers)

    print("\nWARNING Not bidmas, execute in order of seeing")


if __name__ == "__main__":
    while True:
        # solve(500, [1, 2, 3, 4, 10, 50])
        # solve(773, [3, 10, 1, 1, 8, 10]) # (10 + 1) * (8 - 1) * 10 + 3
        play()
