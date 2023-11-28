#!/usr/bin/env python3

"""
Test your implementation of the missionaries problem by piping your
output through this program.


"""

import re
import sys


def test_three(crossings: list) -> bool:
    m_near = c_near = 3
    m_far = c_far = 0
    print("Prints (cannibals, missionaries) in each output pair.")

    for i, cross in enumerate(crossings):
        if i % 2 == 0:  # from near to far
            c_near -= cross[0]
            c_far += cross[0]
            m_near -= cross[1]
            m_far += cross[1]
        else:  # from far to near.
            c_near += cross[0]
            c_far -= cross[0]
            m_near += cross[1]
            m_far -= cross[1]

        if i % 2 == 0:
            print(f"{i}. send {cross}. near bank: {(c_near, m_near)}, far bank: {(c_far, m_far)}")
        else:
            print(f"{i}. {cross} returns. near bank: {(c_near, m_near)}, far bank: {(c_far, m_far)}")
        sys.stdout.flush()

        if c_near > m_near > 0:
            return False
        if c_far > m_far > 0:
            return False

    return  c_near == m_near == 0 and c_far == m_far == 3


xings = []   # "xings" == "crossings"
for line in sys.stdin:
    # Find all integers in the line
    numbers = re.findall(r'\b\d+\b', line)

    # Check if we have at least two integers
    if len(numbers) >= 2:
        c, m = list(map(int, numbers[:2]))
        xings.append((m,c))
    else:
        print("Not enough integers found in the line.")

if test_three(xings):
    print("Passed")
else:
    print("Failed")



