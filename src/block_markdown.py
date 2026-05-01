from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "orderered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    striped_blocks = []
    for block in blocks:
        block = block.strip('\n ') #newline and whitespcaes
        if block != "":
            striped_blocks.append(block)
    return striped_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    #heading
    if block[0] == "#":
        for i in range(6):
            if block[i] == "#" and block[i+1] == " ":
                return BlockType.HEADING
    #code
    if len(lines) > 0 and lines[0].startswith("```") and block.endswith("```"):
        return BlockType.CODE

    #quote
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    #unordered list
    if block.startswith("-"):
        for line in lines:
            if not line.startswith("-"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    #ordered list
    if block.startswith("1. "):
        for i in range(1,len(lines)+1):
            if not lines[i].startswith(f"{i}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
