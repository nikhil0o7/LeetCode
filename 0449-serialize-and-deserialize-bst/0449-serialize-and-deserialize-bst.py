# class TreeNode:
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def preorder(node) -> None:
            if not node:
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        print(res)
        return ",".join(res)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return []

        vals = []

        for x in data.split(","):
            vals.append(int(x))

        print(vals)
        self.i = 0
        def build(lower,upper) -> Optiona[TreeNode]:
            if self.i == len(vals):
                return None
            val = vals[self.i]

            if val < lower or val > upper:
                return None
            
            self.i +=1
            node = TreeNode(val)
            left = build(lower,val)
            right = build(val, upper)
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