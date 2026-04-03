import unittest

from htmlnode import *
from textnode import *

class TestHTMLNode(unittest.TestCase):
    # html node tests
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

    # leaf node tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Link to website", {"href": "boot.dev"})
        self.assertEqual(node.to_html(), '<a href="boot.dev">Link to website</a>')

    # parent node tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_grandchildren(self):
        grandchild_node_one = LeafNode("b", "grandchild_one")
        grandchild_node_two = LeafNode("i", "grandchild_two")
        child_node = ParentNode("span", [grandchild_node_one, grandchild_node_two])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild_one</b><i>grandchild_two</i></span></div>",
        )

    def test_to_html_with_no_grandchildren(self):
        child_node = ParentNode("span", None)
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(
                ValueError,
                parent_node.to_html,
                )

if __name__ == "__main__":
    unittest.main()
