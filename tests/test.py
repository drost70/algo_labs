import unittest

from src.main import BinaryTree, invert_binary_tree


class TestBinaryTreeOperations(unittest.TestCase):
    def test_invert_binary_tree_new_case(self):
        root = BinaryTree(8)
        root.left = BinaryTree(9)
        root.right = BinaryTree(10)
        root.left.left = BinaryTree(11)
        root.left.right = BinaryTree(12)
        root.right.left = BinaryTree(13)
        root.right.right = BinaryTree(14)

        inverted_tree = invert_binary_tree(root)

        expected_tree = BinaryTree(8)
        expected_tree.left = BinaryTree(10)
        expected_tree.right = BinaryTree(9)
        expected_tree.left.left = BinaryTree(14)
        expected_tree.left.right = BinaryTree(13)
        expected_tree.right.left = BinaryTree(12)
        expected_tree.right.right = BinaryTree(11)

        self.assertTrue(self.is_equal(inverted_tree, expected_tree))

    def test_invert_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        inverted_tree = invert_binary_tree(root)

        expected_tree = BinaryTree(1)
        expected_tree.left = BinaryTree(3)
        expected_tree.right = BinaryTree(2)
        expected_tree.left.left = BinaryTree(7)
        expected_tree.left.right = BinaryTree(6)
        expected_tree.right.left = BinaryTree(5)
        expected_tree.right.right = BinaryTree(4)

        self.assertTrue(self.is_equal(inverted_tree, expected_tree))

    def is_equal(self, tree1: BinaryTree, tree2: BinaryTree) -> bool:
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False

        return tree1.value == tree2.value and self.is_equal(tree1.left, tree2.left) and self.is_equal(tree1.right,
                                                                                                      tree2.right)


if __name__ == '__main__':
    unittest.main()
