class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self.tree = None

        for d in tree_data:
            self.tree = self.insert(d, self.tree)

    def insert(self, item, tree):
        if tree is None:
            return TreeNode(item, None, None)

        elif item <= tree.data:
            tree.left = self.insert(item, tree.left)

        else:
            tree.right = self.insert(item, tree.right)

        return tree

    def traverse_tree(self, tree):
        return_data = []
        if tree.left:
            return_data += self.traverse_tree(tree.left)

        return_data += [tree.data]

        if tree.right:
            return_data += self.traverse_tree(tree.right)

        return return_data

    def data(self):
        return self.tree

    def sorted_data(self):
        return self.traverse_tree(self.tree)


if __name__ == '__main__':
    b = BinarySearchTree(['2', '2'])
    print(b.sorted_data())