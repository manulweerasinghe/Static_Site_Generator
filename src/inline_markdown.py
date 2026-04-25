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
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            section = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(section) != 2:
                raise ValueError("invalid image markdown")
            if section[0] != "":
                new_nodes.append(TextNode(section[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMG_FORMAT, image[1]))
            original_text = section[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))
    return new_nodes
def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            section = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(section) != 2:
                raise ValueError("invalid link markdown")
            if section[0] != "":
                new_nodes.append(TextNode(section[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK_FORMAT, link[1]))
            original_text = section[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))
    return new_nodes
