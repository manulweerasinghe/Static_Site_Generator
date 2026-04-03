class HTMLNode:
    def __init__(self, tag = None, val = None, child = None, props = None):
        self.tag = tag
        self.value = val
        self.children = child
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method is not implemented")

    def props_to_html(self):
        fstring = ""
        if not self.props is None:
            for prop in self.props:
                fstring += f' {prop}="{self.props[prop]}"'
        return fstring

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, val, props = None):
        super().__init__(tag, val, props = props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node must have a value")
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent node must have a tag")

        if self.children is None:
            raise ValueError("parent node must have a children")
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
