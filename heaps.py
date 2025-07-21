def heap_recursive(k, array):
    if k == 1:
        yield array
    else:
        # heap_recursive(k - 1, array)

        for i in range(k - 1):
            yield from heap_recursive(k - 1, array)
            if k % 2 == 0:
                array[i], array[k - 1] = array[k - 1], array[i]
            else:
                array[0], array[k - 1] = array[k - 1], array[0]

        yield from heap_recursive(k - 1, array)


a = [1, 2, 3]
print(list(heap_recursive(len(a), a)))


def heap_iterative(n, array):
    c = [0 for _ in range(n)]

    yield array

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                array[0], array[i] = array[i], array[0]
            else:
                array[c[i]], array[i] = array[i], array[c[i]]
            yield array

            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1


b = ['a', 'b', 'c']
print(list(heap_iterative(len(b), b)))