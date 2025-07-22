from itertools import permutations
from operator import mul, truediv, add, sub

from multiprocessing import Pool

import sys
import ctypes


# TODO 4-4s / nubble with stack based theory
# TODO format to release in order of length

rpn = ctypes.CDLL("./rpn_evaluator.so")
rpn.evaluate.argtypes = (ctypes.c_char_p,)
rpn.evaluate.restype = ctypes.c_int


operations = [
    ("+", add),
    ("-", sub),
    ("*", mul),
    ("/", truediv),
]


def to_string(expr):
    if type(expr) is int:
        return str(expr)
    left, op, right = expr
    return f"({to_string(left)} {op} {to_string(right)})"


def all_expressions_rpn(numbers):
    if len(numbers) == 1:
        return [str(numbers[0])]

    expressions = []
    for i in range(1, len(numbers)):
        left_parts = all_expressions_rpn(numbers[:i])
        right_parts = all_expressions_rpn(numbers[i:])
        for left_part in left_parts:
            for right_part in right_parts:
                for op, _ in operations:
                    # Prune commutative duplicates
                    if op in ("+", "*") and left_part > right_part:
                        continue
                    expr = f"{left_part} {right_part} {op}"
                    expressions.append(expr)
    return expressions


def generate_all_rpn_expressions(numbers):
    """Generates RPN strings for all permutations and all subset lengths."""
    seen = set()
    results = []
    for r in range(1, len(numbers) + 1):
        for perm in permutations(numbers, r):
            exprs = all_expressions_rpn(list(perm))
            for e in exprs:
                if e not in seen:
                    seen.add(e)
                    results.append(e)
    return results


def solve(target, numbers):
    seen = set()
    for perm in permutations(numbers):
        exprs = generate_all_rpn_expressions(list(perm))
        for expr in exprs:
            if expr in seen:
                continue
            seen.add(expr)
            val = rpn.evaluate(expr.encode("utf-8"))
            if val == target:
                print(f"{expr} = {target}")


def play():
    try:
        numbers = [int(x) for x in input("Numbers: ").split()]
    except ValueError:
        sys.exit()

    target = int(input("Target: "))

    solve(target, numbers)


if __name__ == "__main__":
    while True:
        # solve(500, [1, 2, 3, 4, 10, 50])
        solve(773, [3, 10, 1, 1, 8, 10])  # (10 + 1) * (8 - 1) * 10 + 3
        exit(0)
        play()
