class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None

    tree.left, tree.right = invert_binary_tree(tree.right), invert_binary_tree(tree.left)

    return tree


def print_binary_tree(tree, level=0, prefix="Root: ") -> None:
    if tree is not None:
        if level == 0:
            print(prefix + str(tree.value))
        else:
            print(" " * (level * 4) + prefix + str(tree.value))
        if tree.left is not None or tree.right is not None:
            if tree.left is not None:
                print_binary_tree(tree.left, level + 1, "Left: ")
            if tree.right is not None:
                print_binary_tree(tree.right, level + 1, "Right: ")


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

print("Binary Tree:")
print_binary_tree(root)

inverted_tree = invert_binary_tree(root)

print("\nInverted Binary Tree:")
print_binary_tree(inverted_tree)
