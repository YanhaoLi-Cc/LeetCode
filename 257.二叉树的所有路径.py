#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
    
    def traversal(self, cur, path, result) -> None:
        path.append(cur.val)
        if not cur.left and not cur.right: # 到达叶子节点
            spath = '->'.join(map(str,path))
            result.append(spath)
            return
        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop()
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop()
# class Solution:
    
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         stack = [root]
#         path_stack = [str(root.val)]
#         result = []
        
#         while stack:
#             cur = stack.pop()
#             path = path_stack.pop()
            
#             if not cur.right and not cur.left:
#                 result.append(path)
#             if cur.right:
#                 stack.append(cur.right)
#                 path_stack.append(path+'->'+str(cur.right.val))            
#             if cur.left:
#                 stack.append(cur.left)
#                 path_stack.append(path+'->'+str(cur.left.val))
#         return result
                

# @lc code=end

