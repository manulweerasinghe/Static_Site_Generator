import re

from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_nodes = []
        # only split the plain text
        if node.text_type == TextType.PLAIN_TEXT:
            split_word = node.text.split(delimiter)
            if len(split_word) % 2 == 0:
                raise Exception("invalid markdown syntax")
            for i in range(len(split_word)):
                if split_word[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(split_word[i], TextType.PLAIN_TEXT))
                else:
                    split_nodes.append(TextNode(split_word[i], text_type))
        else:
            split_nodes.append(node)
        new_nodes.extend(split_nodes) # add all the splited elementes
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
