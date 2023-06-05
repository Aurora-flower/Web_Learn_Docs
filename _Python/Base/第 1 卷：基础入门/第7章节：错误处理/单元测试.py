import unittest
from T1 import myAdd


class MyTestCase(unittest.TestCase):
    def test_myAdd(self):
        result = myAdd(3, 2)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
