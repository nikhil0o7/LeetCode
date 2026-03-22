# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def preorder(node) -> None:
            if not node:
                return

            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        print(res)
        return "".join(res)



    def deserialize(self, data):
        if not data:
            return []

        vals = [int(x) for x in data.split(",")]
        self.i = 0
        def build(lower,upper) -> Optional[TreeNode]:
            if self.i == len(vals):
                return  None

            val = vals[self.i]
            if val < lower or val > upper:
                return None
            self.i += 1
            node = TreeNode(val)    
           
            left = build(lower,val)
            right = build(val, lower)
            node.left = left
            node.right = right
            return node
        return build(float("-inf"),float("inf"))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans