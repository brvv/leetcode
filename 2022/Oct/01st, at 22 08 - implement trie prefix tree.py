class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        self._is_last = False
    
    def setLast(self, val):
        self._is_last = val
    
    def isLast(self):
        return self._is_last
    
    def getVal(self):
        return self.val
    
    def getChild(self, childVal):
        for child in self.children:
            if child.getVal() == childVal:
                return child
        return None
    
    def insertChild(self, childVal):
        child = self.getChild(childVal)
        
        if child is None:
            self.children.append((TrieNode(childVal)))
            child = self.children[-1]
        return child
        

class Trie:

    def __init__(self):
        self.parentNode = TrieNode("parent")
        

    def insert(self, word: str) -> None:
        current_node = self.parentNode.insertChild(word[0])
        
        for letter in word[1::]:
            new_node = current_node.insertChild(letter)
            current_node = new_node
            
        current_node.setLast(True)
        
            
        
        

    def search(self, word: str) -> bool:
        current_node = self.parentNode
        
        for letter in word:
            child = current_node.getChild(letter)
            if child is None:
                return False
            current_node = child
        return current_node.isLast()
        

    def startsWith(self, prefix: str) -> bool:
        current_node = self.parentNode
        
        for letter in prefix:
            child = current_node.getChild(letter)
            if child is None:
                return False
            current_node = child
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)