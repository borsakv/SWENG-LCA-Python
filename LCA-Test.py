import unittest
from LCA import Node
from LCA import findPath
from LCA import findLCA

class TestLCA(unittest.TestCase):
    def testInsert(self):
        # Asserting insert
        root = Node(40)
        self.assertEquals(root.data, 40)
        root.insert(20)
        self.assertEquals(root.left.data, 20)

    root = Node(40)
    root.insert(20)
    root.insert(10)
    root.insert(30)
    root.insert(60)
    root.insert(50)
    root.insert(70)
    root.insert(5)
    root.insert(45)
    root.insert(55) 
    """
                       40
                   /      \
                20         60
               /  \      /  \
              10   30  50   70
            /          \
            5           55

    """

    def testFindPath(self):
        path = []
        # Asserting FindPath function for a existing node
        self.assertTrue(findPath(self.root, path, 55))
        # Asserting FindPath function for a non-existing node
        self.assertFalse(findPath(self.root, path, 12))
        # Asserting FindPath function for a Float
        self.assertFalse(findPath(self.root, path, 30.46))
        # Asserting FindPath function for a String
        self.assertFalse(findPath(self.root, path, "String"))
        # Asserting FindPath function for a char
        self.assertFalse(findPath(self.root, path, 'char'))


    def testLCATrue(self):
        # Asserting LCA using two real nodes in the tree
        self.assertEquals(findLCA(self.root, 5, 30), 20)
        self.assertEquals(findLCA(self.root, 55, 70), 60)

    def testLCAFake(self):
        # Asserting LCA using two fake nodes in the tree
        self.assertEquals(findLCA(self.root, 7, 1), -1)
        # Asserting LCA using one fake node and one existing node in the tree
        self.assertEquals(findLCA(self.root, 7, 30), -1)
        # Asserting LCA using one fake node and one existing node in the tree
        self.assertEquals(findLCA(self.root, 50, 1), -1)

    def testLCANonint(self):
        # Asserting LCA using floats
        self.assertEquals(findLCA(self.root, 55.05, 70.5), -1)
        # Asserting LCA using Strings
        self.assertEquals(findLCA(self.root, "String", "String"), -1)   
        # Asserting LCA using chars
        self.assertEquals(findLCA(self.root, 'char', 'char'), -1)


if __name__ == '__main__':
    unittest.main()