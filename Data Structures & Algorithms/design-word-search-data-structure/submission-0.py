class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWordEnd = True

    def search_helper(self,node, word: str) -> bool:
        if word == "":
            return node.isWordEnd
        if word[0] == '.':
            found = False
            for child in node.children:
                ret = self.search_helper(node.children[child],word[1:])
                if ret:
                    found = True
            return found
        if word[0] not in node.children:
            return False
        return self.search_helper(node.children[word[0]],word[1:])

    def search(self, word: str) -> bool:
        return self.search_helper(self.root,word)
        
