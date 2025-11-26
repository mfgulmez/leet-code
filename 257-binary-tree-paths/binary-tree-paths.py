# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def paths(self, treeNode, path, paths):
        if treeNode == None:
            return
        else:
            if treeNode.left == None and treeNode.right == None:
                path += str(treeNode.val)
                paths.append(path)
            elif treeNode.left == None:
                path += str(treeNode.val) + "->"
                self.paths(treeNode.right, path, paths)
            elif treeNode.right == None:
                path += str(treeNode.val) + "->"
                self.paths(treeNode.left, path, paths)
            else:
                path += str(treeNode.val) + "->"
                self.paths(treeNode.left, path, paths)
                self.paths(treeNode.right, path, paths)
        
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        path, paths = "", []
        self.paths(root, path, paths)
        return paths