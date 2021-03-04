from operator import mul, truediv, add, sub
from itertools import permutations
from time import time
import sys

print("+++ WARNING +++")
print("+++ NOT bidmas, operators executed in displayed order! +++", '\n')


def mydiv(a, b):
    result = truediv(a, b)
    if int(result) == result:
        return int(result)
    else:
        raise ValueError


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

    for x in numbers:
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

# numbers = permutations([100, 25, 6, 5, 3, 9])
# results = []
# for x in numbers:
#     for y in all_ops:
#         try:
#             temp_out = y[4](y[3](y[2](y[1](y[0](x[0], x[1]), x[2]), x[3]), x[4]), x[5])
#             if int(temp_out) == temp_out and temp_out > 0:
#                 results.append((temp_out, str(x[0])+op_translate[y[0]] + str(x[1])+op_translate[y[1]] + str(x[2])+op_translate[y[2]] + str(x[3])+op_translate[y[3]] + str(x[4])+op_translate[y[4]] + str(x[5])))
#         except ValueError:
#             pass
#
# print(results)
