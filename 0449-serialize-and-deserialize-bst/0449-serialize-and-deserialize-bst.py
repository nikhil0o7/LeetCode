# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []

        def preorder(node):
            if not node:
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(res)

        

    def deserialize(self, data):
        if not data:
            return None

        vals = list(map(int, data.split(",")))
        self.i = 0

        def build(lower, upper):
            if self.i == len(vals):
                return None

            val = vals[self.i]

            # BST constraint
            if val < lower or val > upper:
                return None

            self.i += 1
            node = TreeNode(val)

            node.left = build(lower, val)
            node.right = build(val, upper)

            return node

        return build(float("-inf"), float("inf"))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans