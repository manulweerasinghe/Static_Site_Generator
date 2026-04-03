from textnode import *
from htmlnode import *
def main():
    tmp = TextNode("This is some anchor text", TextType.LINK_FORMAT, "https://www.boot.dev")
    print(tmp)

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
if __name__ == "__main__":
    main()
