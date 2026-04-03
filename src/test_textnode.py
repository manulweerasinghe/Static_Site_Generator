import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_dif(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node1 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node1)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.LINK_FORMAT)
        node1 = TextNode("This is a text node", TextType.LINK_FORMAT)
        self.assertEqual(node.url, node1.url)

    def test_url_dif(self):
        node = TextNode("This is a text node", TextType.LINK_FORMAT, "url.com")
        node1 = TextNode("This is a text node", TextType.LINK_FORMAT)
        self.assertNotEqual(node.url, node1.url)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_error(self):
        node = TextNode("This is a text node", TextType.TEST_ERROR)
        self.assertRaises(
                Exception,
                text_node_to_html_node, node,
                )

    def test_image(self):
        node = TextNode("This is an image", TextType.IMG_FORMAT, "the.url.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"scr":"the.url.com", "alt": "This is an image"})
if __name__ == "__main__":
    unittest.main()
