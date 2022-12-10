import unittest
from main import schitat


class MyTestCase(unittest.main):

    def test_something(self):
        self.assertEqual(schitat(5670000), 4)


if __name__ == '__main__':
    unittest.main()
