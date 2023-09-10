

import unittest

from P11_v2 import HalfAdder, Connector, Source


class TestP11v2(unittest.TestCase):

    def test_halfadder(self):
        source1 = Source("S1")
        source2 = Source("S2")
        hadder = HalfAdder("HA")
        Connector(source1, hadder)
        Connector(source2, hadder)
        source1.set(0)
        source2.set(0)

        out, carry = hadder.getOutput()
        self.assertEqual(out, 0)
        self.assertEqual(carry, 0)

        source1.set(0)
        source2.set(1)

        out, carry = hadder.getOutput()
        self.assertEqual(out, 1)
        self.assertEqual(carry, 0)

        source1.set(1)
        source2.set(0)

        out, carry = hadder.getOutput()
        self.assertEqual(out, 1)
        self.assertEqual(carry, 0)

        source1.set(1)
        source2.set(1)

        out, carry = hadder.getOutput()
        self.assertEqual(out, 0)
        self.assertEqual(carry, 1)
