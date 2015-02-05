import unittest


class Stack(object):

    def __init__(self):
        self.items = []
        self.maxs = []

    def push(self, item):
        """push a new item to the last index
        """
        if (self.maxs and item > self.maxs[-1]) or not self.maxs:
            self.maxs.append(item)
        self.items.append(item)

    def pop(self):
        """remove the last item
        """
        if not self.items:
            return None

        item = self.items.pop()
        if item == self.maxs[-1]:
            self.maxs.pop()

        return item

    def peek(self):
        """see what the last item is
        """
        if not self.items:
            return None

        return self.items[-1]

    def get_max(self):
        return self.maxs and self.maxs[-1] or None


class Tests(unittest.TestCase):

    def test_get_max(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        self.assertEqual(stack.get_max(), 9)

        stack.push(9)
        self.assertEqual(stack.get_max(), 9)

        stack.pop()
        stack.pop()
        self.assertEqual(stack.get_max(), 8)


if __name__ == '__main__':
    unittest.main()
