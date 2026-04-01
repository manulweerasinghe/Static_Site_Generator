import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
