import unittest

from block_markdown import *
from blocktype import *
class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_markdown_with_extra_newlines(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_blocktype_paragraph(self):
        md = "This is a paragraph"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_blocktype_lists(self):
        md = """
- The first element
- The second element

1. This is first order item
2. This is second order item

3. This will be a paragraph
4. This also
"""
        blocks = markdown_to_blocks(md)
        blocktype_list = []
        for block in blocks:
            blocktype_list.append(block_to_block_type(block))
        self.assertListEqual(blocktype_list, [BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST, BlockType.PARAGRAPH])

    def test_blocktype_headings(self):
        md = """
# Heading 1

###### Heading 6

####### Heading 7
"""
        blocks = markdown_to_blocks(md)
        blocktype_list = []
        for block in blocks:
            blocktype_list.append(block_to_block_type(block))
        self.assertListEqual(blocktype_list, [BlockType.HEADING, BlockType.HEADING, BlockType.PARAGRAPH])

    def test_blocktpye_code(self):
        md = """```
This is the code block
Another line```
"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_blocktype_quote(self):
        md = """> This is a quote
>This is another one, wothout a space"""
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)
