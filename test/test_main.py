import unittest
from main import main


class TestMain(unittest.TestCase):

    def test_invalid_args(self):
        main()


if __name__ == "__main__":
    unittest.main()
