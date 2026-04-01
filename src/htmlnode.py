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
                fstring += f' {prop}="{self.props[prop]}" '
        return fstring

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
