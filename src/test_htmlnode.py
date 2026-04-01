import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node1 = HTMLNode()
        self.assertEqual(node.props_to_html(), node1.props_to_html())

    def test_eq_link(self):
        node = HTMLNode("a", props = {"href":"boot.dev"})
        node1 = HTMLNode("a",props = {"href":"boot.dev"})
        self.assertEqual(node.props_to_html(), node1.props_to_html())

    def test_dif_link(self):
        node = HTMLNode("a", props = {"href":"google.com"})
        node1 = HTMLNode("a",props = {"href":"boot.dev"})
        self.assertNotEqual(node.props_to_html(), node1.props_to_html())
if __name__ == "__main__":
    unittest.main()
