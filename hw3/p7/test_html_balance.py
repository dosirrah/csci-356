import unittest
from html_balance import html_balance
import os
import tempfile


class TestHTMLBalance(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for this test
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)  # Ensure the directory is cleaned up after tests

    def test_html_balance_empty(self):
        new_file_path = os.path.join(self.temp_dir.name, 'empty.html')
        with open(new_file_path, "w") as fp:
            pass   # empty file.

        self.assertTrue(html_balance(new_file_path))

    def test_html_balance_bad(self):
        self.assertFalse(html_balance("bad.html"))
        self.assertFalse(html_balance("bad2.html"))

    def test_html_balance_valid(self):
        self.assertTrue(html_balance("valid.html"))
        self.assertTrue(html_balance("valid2.html"))
