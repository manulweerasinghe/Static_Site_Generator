from enum import Enum
import re
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "orderered list"

def block_to_block_type(block):
    #heading
    if block[0] == "#":
        for i in range(6):
            if block[i] == "#" and block[i+1] == " ":
                return BlockType.HEADING
    #code
    #code = re.findall(r"\`{3}\n([^\`]*)\`{3}", block)
    if block[0] == "`":
        for i in range(3):
            if block[i] == "`" and block[i+1] == "\n":
                return BlockType.CODE
    #quote
    quote = re.findall(r"\>(.*)", block)
    if len(quote) != 0:
        return BlockType.QUOTE

    #unordered list
    unordered = re.findall(r"\-\s(.*)", block)
    if len(unordered) != 0:
        return BlockType.UNORDERED_LIST

    #unordered list
    ordered = re.findall(r"\d\.\s(.*)", block)
    if len(ordered) != 0 and block[0] == "1":
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
