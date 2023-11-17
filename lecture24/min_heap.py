"""Based on the BinHeap class implemented in section 7.10 of
   runstone academy's *Problem Solving with Algorithms and Data Structures using Python*
   by Miller and Ranum.  However, I modified parts to be inline with PEP 8
   conventions.  This means using snake case in method and variable names
   and preceding private member variables with a an underscore.

   I also renamed insert to push and delMin to pop.  It is more common
   to talk about pushing and popping."""


class MinHeap:
    def __init__(self):
        self._heap = [0]
        self._len = 0

    def __len__(self) -> int:
        return self._len

    def push(self, k) -> None:
        self._heap.append(k)     # amortized O(1) list append
        self._len += 1           # O(1) increment
        self._perc_up(self._len) # ?

    # The book calls this delMin, but the standard term is "pop".
    # To pop, swap the rightmost element in the bottom level to the top
    # and percolate it downward.
    def pop(self) -> object:
        if self._len == 0:                     # (1)
            raise IndexError                   # (2)
        retval = self._heap[1]                 # (3)
        self._heap[1] = self._heap[self._len]  # (4)
        self._len -= 1                         # (5)
        self._heap.pop()                       # (6)
        self._perc_down(1)                     # (7)
        return retval                          # (8)

    def _perc_up(self, i) -> None:
        while i // 2 > 0:                             # (1) T_1 = ? * O(1) division and compare
            if self._heap[i] < self._heap[i // 2]:    # (2) O(1) compare
                self._heap[i], self._heap[i // 2] = self._heap[i // 2], self._heap[i] # (3) O(1) swap
            i = i // 2                                # (4) O(1) division

    def _perc_down(self, i) -> None:
        while (i * 2) <= self._len:                  # (1)
            mc = self._min_child(i)                  # (2)
            if self._heap[i] > self._heap[mc]:       # (3)
                self._heap[mc], self._heap[i] = self._heap[i], self._heap[mc]
            i = mc                                   # (5)

    def _min_child(self, i) -> int:
        if i * 2 + 1 > self._len:              # (1)
            return i * 2                       # (2)
        else:                                  # (3)
            if self._heap[i * 2] < self._heap[i * 2 + 1]:
                return i * 2                   # (5)
            else:                              # (6)
                return i * 2 + 1               # (7)

    def make_heap(self, items : list):
        if len(items) == 0:          # (1)  1 comparison + 1 len
            return                   # (2)
        self._heap = [0]             # (3)  1 step
        self._heap.extend(items)     # (4)  O(n)
        self._len = len(items)       # (5)  1 step
        i = self._len // 2           # (6)  1 division + 1 assign
        while i > 0:                 # (7)  n//2*(1 comp + from (8)-(9) )
            self._perc_down(i)       # (8)  ?
            i = i - 1                # (9)  1 subtract + 1 assign