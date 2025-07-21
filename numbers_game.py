from itertools import permutations
from operator import mul, truediv, add, sub
import sys


# TODO 4-4s / nubble with stack based theory
# TODO format to release in order of length


operations = [
    ("+", add),
    ("-", sub),
    ("*", mul),
    ("/", truediv),
]


# Expression tree represented as tuples: (left_expr, operator, right_expr)
def evaluate(expr):
    if type(expr) is int:
        return expr
    left, op, right = expr
    try:
        l_val = evaluate(left)
        r_val = evaluate(right)
        if l_val is None or r_val is None or l_val < 0 or r_val < 0:
            return None
        if op == "/" and r_val == 0:
            return None
        result = dict(operations)[op](l_val, r_val)
        if int(result) != result:  # countdown only allows integers
            return None
        return int(result)
    except ZeroDivisionError:
        return None


def to_string(expr):
    if type(expr) is int:
        return str(expr)
    left, op, right = expr
    return f"({to_string(left)} {op} {to_string(right)})"


def all_expressions(numbers):
    if len(numbers) == 1:
        return [numbers[0]]

    expressions = []
    for i in range(1, len(numbers)):
        left_parts = all_expressions(numbers[:i])
        right_parts = all_expressions(numbers[i:])
        for l in left_parts:
            for r in right_parts:
                for op, _ in operations:
                    expressions.append((l, op, r))
    return expressions


def solve(target, numbers):
    seen = set()
    for perm in permutations(numbers):
        exprs = all_expressions(list(perm))
        for expr in exprs:
            val = evaluate(expr)
            if val == target:
                expr_str = to_string(expr)
                if expr_str not in seen:
                    seen.add(expr_str)
                    print(f"{expr_str} = {target}")


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
        solve(773, [3, 10, 1, 1, 8, 10]) # (10 + 1) * (8 - 1) * 10 + 3
        exit(0)
        # play()
