from enum import Enum
from htmlnode import *

class TextType(Enum):
    PLAIN_TEXT = "plain text"
    BOLD_TEXT = "bold text"
    ITALIC_TEXT = "italic text"
    CODE_TEXT = "code text"
    LINK_FORMAT = "link"
    IMG_FORMAT = "image"
    TEST_ERROR = "error"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text_type == other.text_type

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(tag = None, val = text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode(tag = "b", val = text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode(tag = "i", val = text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode(tag = "code", val = text_node.text)
        case TextType.LINK_FORMAT:
            return LeafNode(tag = "a", val = text_node.text)
        case TextType.IMG_FORMAT:
            return LeafNode(tag = "img", val = "", props = {"scr": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid text_type")
