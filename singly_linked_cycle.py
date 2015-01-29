"""
Write a function contains_cycle() that takes the first node
in a singly-linked list and returns a boolean indicating
whether the list contains a cycle.


The solution shown here is not optimal. The following solution runs in O(n)
time, which is optimal, but uses O(n) space. An algorithm exists that runs
in O(n) time and only uses O(1) space.
I've also added an id attribute to the Node class, which is not needed. One
can keep track of the seen nodes using a hashmap.

"""

import unittest


class Node(object):

    def __init__(self, id, next, data):
        self.id = id
        self.next = next
        self.data = data


def contains_cycle(first_node):
    # build a set of all seen ids
    seen_nodes = set([first_node.id])
    next_node = first_node.next

    while next_node.next is not None:
        node = next_node
        seen_nodes.add(node.id)
        next_node = node.next
        if next_node.id in seen_nodes:
            # if we find a next with a seen id, assume a cycle
            return True

    return False


class Tests(unittest.TestCase):

    def create_nested_node(self, child_id, parent_node):
        child_node = Node(child_id, None, 'foo')
        parent_node.next = child_node
        return child_node

    def create_linked_list(self):
        node = Node(0, None, 'foo')
        first_node = node
        for idx in range(1, 10):
            node = self.create_nested_node(idx, node)
        return (first_node, node)

    def test_cycle(self):
        first_node, last_node = self.create_linked_list()
        last_node.next = first_node
        self.assertTrue(contains_cycle(first_node))

    def test_no_cycle(self):
        first_node, last_node = self.create_linked_list()
        last_node.next = None
        self.assertFalse(contains_cycle(first_node))


if __name__ == '__main__':
    unittest.main()
