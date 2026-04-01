import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is a paragraph")
        node1 = HTMLNode("p", "this is a paragraph")
        self.assertEqual(node, node1)

if __name__ == "__main__":
    unittest.main()
