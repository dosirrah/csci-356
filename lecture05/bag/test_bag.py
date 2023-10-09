# As an example of Test-Driven Development (TDD), I started writing tests write
# after deciding on a basic programming interface to the Bag class.
# I will flesh out Bag.py as I add tests.  This will do this
# in class on Thursday, September 7.

import unittest
from bag import Bag

class TestBag(unittest.TestCase):

    def test_instantiation(self):
        b = Bag()

    def test_add_and_in(self):
        # I have yet to add any tests here...
        pass
