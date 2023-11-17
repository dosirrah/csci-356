from lecture24.min_heap import MinHeap


def heap_sort_pushes(arr: list):
    h = MinHeap()
    for x in arr:
        h.push(x)

    i = 0
    while len(h) > 0:
        x = h.pop()
        arr[i] = x
        # assert i == 0 or x >= arr[i-1]
        i += 1


def heap_sort(arr: list):
    h = MinHeap()
    h.make_heap(arr)

    i = 0
    while len(h) > 0:
        x = h.pop()
        arr[i] = x
        # assert i == 0 or x >= arr[i-1]
        i += 1
