class HTMLNode:
    def __init__(self, tag = None, val = None, child = None, props = None):
        self.tag = tag
        self.value = val
        self.children = child
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        fstring = ""
        if self.props != None:
            for prop in self.props:
                fstring += f' {prop}="{self.props[prop]}" '
        return fstring

    def __repr__(self):
        return f"tag: {self.tag}, val: {self.value}, children: {self.children}, props: {self.props}"
