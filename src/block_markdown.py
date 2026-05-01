def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    striped_blocks = []
    for block in blocks:
        block = block.strip('\n ') #newline and whitespcaes
        if block != "":
            striped_blocks.append(block)
    return striped_blocks
