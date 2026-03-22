"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""
class WrappableInt:
        def __init__(self, x):
            self.value = x
        def getValue(self):
            return self.value
        def increment(self):
            self.value += 1

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serializedList = []
        self._serializedHelper(root, serializedList)
        return "".join(serializedList)

    def _serializedHelper(self, root, serializedList):
        if not root:
            return
        
        serializedList.append(chr(root.val + 48))

        for child in root.children:
            self._serializedHelper(child,serializedList)

        serializedList.append('#')

	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        return self._deserializedHelper(data, WrappableInt(0))
    
    def _deserializedHelper(self, data, index):
        if index.getValue() == len(data):
            return None

        node = Node(ord(data[index.getValue()])-48, [])
        index.increment()
        while (data[index.getValue()] != '#'):
            node.children.append(self._deserializedHelper(data,index))

        # to discard the #
        index.increment()
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))