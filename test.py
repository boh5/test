class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        global ans

        def dfs(node, prev_total):
            if node is None:
                if prev_total == sum:
                    ans = True
                return
            cur_total = prev_total + node.val
            dfs(node.left, cur_total)
            dfs(node.right, cur_total)

        dfs(root, 0)
        return ans


if __name__ == '__main__':
    so
