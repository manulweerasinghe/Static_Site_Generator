import unittest

from split_delimiter import *
from textnode import *

class TestSplitDilimiter(unittest.TestCase):
    def test_eq(self):
        result = split_nodes_delimiter([TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)], "`", TextType.CODE_TEXT)
        expected = [
        TextNode("This is text with a ", TextType.PLAIN_TEXT),
        TextNode("code block", TextType.CODE_TEXT),
        TextNode(" word", TextType.PLAIN_TEXT),
        ]
        self.assertEqual(result, expected)
