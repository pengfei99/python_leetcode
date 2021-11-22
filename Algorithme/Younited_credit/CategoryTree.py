class CategoryTree:
    class Node:
        def __init__(self, name: str):
            self.name = name
            self.children = []

        def set_child(self, child_name):
            self.children.append(child_name)

        def get_child(self):
            return self.children

    def __init__(self):
        self.node_list = []

    def get_parent(self, name):
        for node in self.node_list:
            if node.name == name:
                return node
            elif name is None:
                return None
            else:
                raise KeyError

    def has_category(self, category):
        for node in self.node_list:
            if node.name == category:
                return True
            else:
                return False

    def add_category(self, category, parent):
        if parent is None:
            root = self.Node(category)
            self.node_list.append(root)
        elif self.has_category(category):
            raise KeyError
        else:
            self.node_list.append(self.Node(category))
            parent_node = self.get_parent(parent)
            parent_node.set_child(category)

    def get_children(self, parent):
        for item in self.node_list:
            if item.name == parent:
                return item.get_child()
        return []


if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))
