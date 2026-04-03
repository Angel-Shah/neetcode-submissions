class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        #build the prefix-tree
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows,cols = len(board),len(board[0])
        ans,visited = set(),set()

        def dfs(r,c,node,word):
            if (r<0 or c<0 or r >= rows or c >= cols or
            (r,c) in visited or 
            board[r][c] not in node.children):
                return
            # if (r < 0 or c < 0 or
            # r >= rows or c >= cols or
            #     (r,c) in visited
            #     board[r][c] not in node.children):
            #     return

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                ans.add(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c)) #removing from visted set for backtracking purposes
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(ans)