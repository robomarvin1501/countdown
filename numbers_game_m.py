from operator import mul, truediv, add, sub
from itertools import permutations
from multiprocessing import Pool
import sys

# NOTE WITH MULTIPROCESSING

print("+++ WARNING +++")
print("+++ NOT bidmas, operators executed in displayed order! +++", '\n')


def mydiv(a, b):
    result = truediv(a, b)
    if int(result) == result:
        return int(result)
    else:
        raise ValueError


def finder(numbers_permed):
    global all_ops
    global target

    for x in numbers_permed:
        for y in all_ops:
            try:
                if len(x) == 6:
                    temp_out = y[4](y[3](y[2](y[1](y[0](x[0], x[1]), x[2]), x[3]), x[4]), x[5])
                elif len(x) == 5:
                    temp_out = y[3](y[2](y[1](y[0](x[0], x[1]), x[2]), x[3]), x[4])
                elif len(x) == 4:
                    temp_out = y[2](y[1](y[0](x[0], x[1]), x[2]), x[3])
                elif len(x) == 3:
                    temp_out = y[1](y[0](x[0], x[1]), x[2])
                else:
                    temp_out = 0
                if temp_out == target:
                    equation = ''
                    for s in range(len(x)):
                        if s == len(x) - 1:
                            equation += str(x[s])
                        else:
                            equation += str(x[s]) + op_translate[y[s]]
                    print(temp_out, equation)
                    sys.exit()
            except (ValueError, IndexError) as e:
                pass


ops = [mul, mydiv, add, sub] * 5
all_ops = list(permutations(ops, 5)) + list(permutations(ops, 4)) + list(permutations(ops, 3)) + list(
    permutations(ops, 2))  # --------------Change here for the number of operators needed
op_translate = {
    mul: " x ",
    mydiv: " / ",
    add: " + ",
    sub: " - "
}

while True:
    try:
        numbers = [int(x) for x in input("Numbers: ").split()]
    except ValueError:
        sys.exit()

    target = int(input("Target: "))
    numbers = list(permutations(numbers)) + list(permutations(numbers, 3)) + list(permutations(numbers, 4)) + list(
        permutations(numbers, 5))

    print(type(numbers[0]))
    with Pool(7) as p:
        p.map(finder, numbers)

    # for x in numbers:
    #     for y in all_ops:
    #         try:
    #             if len(x) == 6:
    #                 temp_out = y[4](y[3](y[2](y[1](y[0](x[0], x[1]), x[2]), x[3]), x[4]), x[5])
    #             elif len(x) == 5:
    #                 temp_out = y[3](y[2](y[1](y[0](x[0], x[1]), x[2]), x[3]), x[4])
    #             elif len(x) == 4:
    #                 temp_out = y[2](y[1](y[0](x[0], x[1]), x[2]), x[3])
    #             elif len(x) == 3:
    #                 temp_out = y[1](y[0](x[0], x[1]), x[2])
    #             else:
    #                 temp_out = 0
    #             if temp_out == target:
    #                 equation = ''
    #                 for s in range(len(x)):
    #                     if s == len(x) - 1:
    #                         equation += str(x[s])
    #                     else:
    #                         equation += str(x[s]) + op_translate[y[s]]
    #                 print(temp_out, equation)
    #                 sys.exit()
    #         except (ValueError, IndexError) as e:
    #             pass
