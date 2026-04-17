import unittest

from split_delimiter import *
from textnode import *

class TestSplitDilimiter(unittest.TestCase):
    def test_code(self):
        result = split_nodes_delimiter([TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)], "`", TextType.CODE_TEXT)
        expected = [
        TextNode("This is text with a ", TextType.PLAIN_TEXT),
        TextNode("code block", TextType.CODE_TEXT),
        TextNode(" word", TextType.PLAIN_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_bold(self):
        node = TextNode("This is **bolded and bold**, then again **bolded**.", TextType.PLAIN_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        expected = [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("bolded and bold", TextType.BOLD_TEXT),
                TextNode(", then again ", TextType.PLAIN_TEXT),
                TextNode("bolded", TextType.BOLD_TEXT),
                TextNode(".", TextType.PLAIN_TEXT),
                ]
        self.assertEqual(result, expected)

    def test_bold_and_italic(self):
        node = TextNode("**bolded** & _italic_", TextType.PLAIN_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        result = split_nodes_delimiter(result, "_", TextType.ITALIC_TEXT)
        expected = [
                TextNode("bolded", TextType.BOLD_TEXT),
                TextNode(" & ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                ]
        self.assertEqual(result, expected)
