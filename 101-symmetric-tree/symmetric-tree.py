# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postOrderLeft(self, treeNode, result):
        if treeNode == None:
            result.append(-1)
            return
        
        self.postOrderLeft(treeNode.left, result)
        self.postOrderLeft(treeNode.right, result)
        result.append(treeNode.val)

    def postOrderRight(self, treeNode, result):
        if treeNode == None:
            result.append(-1)
            return
        
        self.postOrderRight(treeNode.right, result)
        self.postOrderRight(treeNode.left, result)
        result.append(treeNode.val)

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.left == None and root.right == None:
            return True

        elif (root.left == None and root.right != None) or (root.left != None and root.right == None):
            return False

        else:
            subtree_left = root.left
            subtree_right = root.right
            result_left = []
            result_right = []
           
            self.postOrderLeft(subtree_left, result_left)
            self.postOrderRight(subtree_right, result_right)
       
            if len(result_left) != len(result_right):
                return False
 
            index = 0
            while index < len(result_left):
                if result_left[index] != result_right[index]:
                    return False
                index += 1
            return True

        