import unittest
import sys
from syncdrive import main


class SyncpyTests(unittest.TestCase):

    def test_no_args(self):
        """run test with no args"""
        self.assertRaises(Exception, main.run, "ok")

    def test_help(self):
        """run test with args --help"""
        sys.argv = "--help"
        self.assertTrue(main.run)


if __name__ == "__main__":
    unittest.main()
