import unittest
from syncpy.syncpy import run


class SyncpyTests(unittest.TestCase):

    def test_invalid_args(self):
        run()


if __name__ == "__main__":
    unittest.main()
