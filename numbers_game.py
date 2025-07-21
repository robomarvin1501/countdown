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


operations = [(add, '+'),
              (sub, '-'),
              (mul, '*'),
              (mydiv, '/')]


def represent_stack(stack):
    reps = [str(item) if type(item) is int else item[1] for item in stack]
    return ' '.join(reps)


def evaluate(stack):
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
    def recurse(stack, nums):
        for n in range(len(nums)):
            stack.append(nums[n])

            remaining = nums[:n] + nums[n + 1:]

            if evaluate(stack) == target:
                print(represent_stack(stack), "= {}".format(target))

            if len(remaining) > 0:
                for op in operations:
                    stack.append(op)
                    stack = recurse(stack, remaining)
                    stack = stack[:-1]

            stack = stack[:-1]

        return stack

    recurse([], numbers)


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
        play()
