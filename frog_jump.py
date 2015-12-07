import math
import unittest


def solution(X, Y, D):
    diff = Y - X
    return int(math.ceil(float(diff)/D))


class Tests(unittest.TestCase):

    def test_one(self):
        self.assertEqual(
            solution(10, 85, 30), 3)


if __name__ == '__main__':
    unittest.main()
