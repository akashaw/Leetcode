'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # for empty Tree
        if not root: return []

        result = [] #store result
        queue = [root] # queue for BFS

        while queue:
            level = [] #store result for current level
            l = len(queue) # number of nodes in current level
            
            for _ in range(l): # scanning nodes in current level and updating queue for their child node
                current_node = queue.pop(0)
                level.append(current_node.val)
                
                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)
            
            result.append(level) # storing result of current level
        return result

