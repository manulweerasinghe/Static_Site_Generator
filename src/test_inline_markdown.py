import unittest

from inline_markdown import *
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

    def test_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMG_FORMAT, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode("second image", TextType.IMG_FORMAT, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
        "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
        TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK_FORMAT, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second link", TextType.LINK_FORMAT, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    # def test_split_link_and_image(self):
    #     node = TextNode(
    #     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
    #     TextType.PLAIN_TEXT,
    #     )
    #     new_nodes = split_nodes_images([node])
    #     new_nodes = split_nodes_links(new_nodes)
    #     self.assertListEqual(
    #         [
    #             TextNode("This is text with an ", TextType.PLAIN_TEXT),
    #             TextNode("image", TextType.IMG_FORMAT, "https://i.imgur.com/zjjcJKZ.png"),
    #             TextNode(" and another ", TextType.PLAIN_TEXT),
    #             TextNode(
    #                 "second link", TextType.LINK_FORMAT, "https://i.imgur.com/3elNhQu.png"
    #             ),
    #         ],
    #         new_nodes,
    #     )
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
                [
        TextNode("This is ", TextType.PLAIN_TEXT),
        TextNode("text", TextType.BOLD_TEXT),
        TextNode(" with an ", TextType.PLAIN_TEXT),
        TextNode("italic", TextType.ITALIC_TEXT),
        TextNode(" word and a ", TextType.PLAIN_TEXT),
        TextNode("code block", TextType.CODE_TEXT),
        TextNode(" and an ", TextType.PLAIN_TEXT),
        TextNode("obi wan image", TextType.IMG_FORMAT, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.PLAIN_TEXT),
        TextNode("link", TextType.LINK_FORMAT, "https://boot.dev"),
        ],
                new_nodes,
                )
if __name__ == "__main__":
    unittest.main()
