from textnode import *
from htmlnode import *
def main():
    tmp = TextNode("This is some anchor text", TextType.LINK_FORMAT, "https://www.boot.dev")
    print(tmp)

if __name__ == "__main__":
    main()
