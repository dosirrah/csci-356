
import unittest
from postfix_calculator import evalate_postfix

class TestPostfixCalculator(unittest.TestCase):
    def test_invalid_expressions(self):
        try:

            evaluate_postfix("")
