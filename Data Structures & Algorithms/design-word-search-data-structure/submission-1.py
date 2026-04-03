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

    def search_helper(self, node, word, idx):
        if idx == len(word):
            return node.isWordEnd
        c = word[idx]
        if c == '.':
            for child in node.children.values():
                if self.search_helper(child, word, idx + 1):
                    return True
            return False
        else:
            if c not in node.children:
                return False
            return self.search_helper(node.children[c], word, idx + 1)

    def search(self, word):
        return self.search_helper(self.root, word, 0)
