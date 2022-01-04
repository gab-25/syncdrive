import unittest
import sys
import os


class SyncpyTests(unittest.TestCase):

    def run_test(self):
        from syncpy import run
        self.assertRaises(Exception, run)

        sys.argv = "--help"
        self.assertTrue(run())


if __name__ == "__main__":
    sys.path.append(os.path.join(os.getcwd(), "syncpy"))
    unittest.main()
