import unittest


def merge_arrays(a, b):
    """We have our lists of orders sorted numerically already,
    in arrays. Write a function to merge our arrays of orders
    into one sorted array.
    """
    merged_array = []
    idx_a = 0
    idx_b = 0

    for i in range(len(a) + len(b)):
        # check if we're at the end of both arrays
        if idx_a == (len(a)) and idx_b == (len(b)):
            continue

        # if a has already been merged, go straight to b
        if idx_a == (len(a)):
            merged_array.append(b[idx_b])
            idx_b += 1
        elif idx_b == (len(b)):
            merged_array.append(a[idx_a])
            idx_a += 1
        elif a[idx_a] < b[idx_b]:
            merged_array.append(a[idx_a])
            idx_a += 1
        else:
            merged_array.append(b[idx_b])
            idx_b += 1

    return merged_array


class Tests(unittest.TestCase):

    def test1(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        expected = merge_arrays(a, b)
        self.assertEqual(expected, [1, 2, 3, 4, 5, 6])

    def test2(self):
        a = [3, 4, 6, 10, 11, 15]
        b = [1, 5, 8, 12, 14, 19]
        expected = merge_arrays(a, b)
        self.assertEqual(expected, [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19])

    def test3(self):
        a = [4, 6, 10, 11, 15]
        b = [1, 5, 8, 12, 14, 19]
        expected = merge_arrays(a, b)
        self.assertEqual(expected, [1, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19])

    def test4(self):
        a = [4, 6, 10, 11, 15]
        b = [4, 5, 8, 12, 14, 19]
        expected = merge_arrays(a, b)
        self.assertEqual(expected, [4, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19])


if __name__ == '__main__':
    unittest.main()
