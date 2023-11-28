from hw4.p2.missionaries import cross_river
import unittest


class TestMissionaries(unittest.TestCase):
    def test_edge_cases(self):
        x = cross_river(1, 1)
        self.assertEqual([(1, 1)], x)

        x = cross_river(1, 0)
        self.assertEqual([(1, 0)], x)

        x = cross_river(0, 1)
        self.assertEqual([(0, 1)], x)

        x = cross_river(2, 0)
        self.assertEqual([(2, 0)], x)

        x = cross_river(0, 2)
        self.assertEqual([(0, 2)], x)

    def test_two(self):
        x = cross_river(2, 2)
        self.assertEqual([(1, 1), (0, 1), (0, 2), (0, 1), (1, 1)], x)

    def test_three(self):
        crosses = cross_river(3, 3)
        m_near = c_near = 3
        m_far = c_far = 0
        for i, cross in enumerate(crosses):
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
            self.assertFalse(c_near > m_near > 0)
            self.assertFalse(c_far > m_far > 0)

        self.assertEqual(0, c_near)
        self.assertEqual(0, m_near)
        self.assertEqual(3, c_far)
        self.assertEqual(3, m_far)
